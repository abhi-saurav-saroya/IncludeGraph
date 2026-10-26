from pathlib import Path
import re

SOURCE_EXTENSIONS = {
    ".c", ".cc", ".cpp", ".cxx",
    ".h", ".hh", ".hpp", ".hxx",
}

PATTERN = r'^\s*#\s*include\s*[<"]([^">]+)[">]'

def discover_cpp_files(project_dir: Path) -> list[Path]:
    if not project_dir.is_dir():
        return []

    discovered_files = []

    for path in project_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in SOURCE_EXTENSIONS:
            discovered_files.append(path)

    return discovered_files


def extract_includes(file_path: Path) -> list[str]:
    includes = []
    contents = file_path.read_text(encoding="utf-8", errors="replace")

    for line in contents.splitlines():
        found_includes = re.findall(PATTERN, line)
        includes.extend(found_includes)

    return includes


def resolve_include(including_file: Path, include_target: str, include_dirs: list[Path]) -> Path | None:
    candidate = including_file.parent / include_target

    if candidate.is_file():
        return candidate

    for dir in include_dirs:
        candidate = dir / include_target
        if candidate.is_file():
            return candidate

    return None


def discover_include_dirs(project_dir: Path) -> list[Path]:
    if not project_dir.is_dir():
        raise NotADirectoryError(
            f"Project directory does not exist: {project_dir}"
        )

    include_dirs = [project_dir]

    for path in project_dir.rglob("*"):
        if path.is_dir():
            # Skip build, version-control and other unnecessary directories.
            if path.name.lower() in {
                "build", "cmake-build-debug", "cmake-build-release",
                ".git", ".vs", "__pycache__", "data"
            }:
                continue

            include_dirs.append(path)

    return include_dirs
            

if __name__ == "__main__":
    project_dir = input("Enter absolute path of the project directory: ")
    project_dir = Path(rf"{project_dir}")
    
    discovered_files = discover_cpp_files(project_dir)
    include_dirs = discover_include_dirs(project_dir)

    for file_path in discovered_files:
        includes = extract_includes(file_path)

        print(f"\n{file_path}")
        for include in includes:
            print(f"  -> {include}")