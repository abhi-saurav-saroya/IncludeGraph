from pathlib import Path

def resolve_include(including_file: Path, include_target: str, include_dirs: list[Path]) -> Path | None:
    candidate = including_file.parent / include_target

    if candidate.is_file():
        return candidate

    for dir in include_dirs:
        candidate = dir / include_target
        if candidate.is_file():
            return candidate

    return None