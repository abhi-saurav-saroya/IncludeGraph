import tempfile
import unittest
from pathlib import Path

from includegraph.parser import extract_includes


class TestExtractIncludes(unittest.TestCase):
    def test_extracts_quoted_and_angle_includes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_file = Path(temp_dir) / "example.cpp"
            source_file.write_text(
                '#include "helper.hpp"\n'
                '#include <iostream>\n'
                'int main() { return 0; }\n',
                encoding="utf-8",
            )

            result = extract_includes(source_file)

            self.assertEqual(
                result,
                ["helper.hpp", "iostream"],
            )

    
    def test_returns_empty_list_when_no_includes_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_file = Path(temp_dir) / "example.cpp"
            source_file.write_text(
                "int main() {\n"
                "    return 0;\n"
                "}\n",
                encoding="utf-8",
            )

            result = extract_includes(source_file)

            self.assertEqual(result, [])



if __name__ == "__main__":
    unittest.main()