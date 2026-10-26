import os
from pathlib import Path

SOURCE_EXTENSIONS = {
    ".c", ".cc", ".cpp", ".cxx",
    ".h", ".hh", ".hpp", ".hxx",
}

EXCLUDED_DIRS = {
    "build", "cmake-build-debug", "cmake-build-release", ".git",
    ".vs", "__pycache__", "data", "assets", "tests", "docs",
    "node_modules", "venv"
}

def discover_cpp_files(project_dir: Path) -> list[Path]:
    if not project_dir.is_dir():
        return []

    discovered_files = []

    for path in project_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in SOURCE_EXTENSIONS:
            discovered_files.append(path)

    return discovered_files

def discover_include_dirs(project_dir: Path) -> list[Path]:
    if not project_dir.is_dir():
        raise NotADirectoryError(
            f"Project directory does not exist: {project_dir}"
        )

    include_dirs = [project_dir]

    for current_dir, dirs, _ in os.walk(project_dir):
        dirs[:] = [
            dir  for dir in dirs
            if dir.lower() not in EXCLUDED_DIRS
        ]

        current_path = Path(current_dir)

        for dir_name in dirs:
            include_dirs.append(current_path / dir_name)

    return include_dirs