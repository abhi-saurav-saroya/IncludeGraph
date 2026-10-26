import re
from pathlib import Path

PATTERN = r'^\s*#\s*include\s*[<"]([^">]+)[">]'


def extract_includes(file_path: Path) -> list[str]:
    includes = []
    contents = file_path.read_text(encoding="utf-8", errors="replace")

    for line in contents.splitlines():
        found_includes = re.findall(PATTERN, line)
        includes.extend(found_includes)

    return includes