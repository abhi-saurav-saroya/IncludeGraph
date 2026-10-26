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
            

if __name__ == "__main__":
    project_dir = input("Enter absolute path of the project directory: ")
    project_dir = Path(rf"{project_dir}")
    
    discovered_files = discover_cpp_files(project_dir)

    for file_path in discovered_files:
        includes = extract_includes(file_path)
    
        print(f"\n{file_path}")
        for include in includes:
            print(f"  -> {include}")