from pathlib import Path

from includegraph.discovery import discover_cpp_files, discover_include_dirs
from includegraph.parser import extract_includes
from includegraph.resolver import resolve_include
            

def main():
    project_dir = input("Enter absolute path of the project directory: ")
    project_dir = Path(rf"{project_dir}")
    
    discovered_files = discover_cpp_files(project_dir)
    include_dirs = discover_include_dirs(project_dir)

    for file_path in discovered_files:
        includes = extract_includes(file_path)

        print(f"\n{file_path}")
        for include in includes:
            resolved_include = resolve_include(file_path, include, include_dirs)
            if resolved_include is not None:
                print(f"  -> {resolved_include}")
            else:
                print(f"  -> {include} (external or unresolved)")


if __name__ == "__main__":
    main()