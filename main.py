from pathlib import Path

SOURCE_EXTENSIONS = {
    ".c", ".cc", ".cpp", ".cxx",
    ".h", ".hh", ".hpp", ".hxx",
}

def discover_cpp_files(project_dir: Path) -> list[Path]:
    if not project_dir.is_dir():
        return []

    discovered_files = []

    for path in project_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in SOURCE_EXTENSIONS:
            discovered_files.append(path)

    return discovered_files
            

if __name__ == "__main__":
    project_dir = input("Enter absolute path of the project directory: ")
    project_dir = Path(rf"{project_dir}")
    
    discovered_files = discover_cpp_files(project_dir)

    for file_path in discovered_files:
        print(f"{file_path}")