import unittest
import tempfile
from click.testing import CliRunner
from ..src.main import wc, count_lines_words_bytes


class TestWcFunctions(unittest.TestCase):

    def test_count_lines_words_bytes(self):
        # Create a temporary file with known content for testing
        with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
            temp_file.write("Hello World!\nThis is a test.")
            temp_file.seek(0)

            lines, words, bytes_count = count_lines_words_bytes(temp_file.name)

            self.assertEqual(lines, 2)
            self.assertEqual(words, 7)
            self.assertEqual(bytes_count, 32)

    def test_wc_with_file(self):
        # Create a temporary file with known content for testing
        with tempfile.NamedTemporaryFile(mode="w+") as temp_file:
            temp_file.write("Hello World!\nThis is a test.")
            temp_file.seek(0)

            runner = CliRunner()
            result = runner.invoke(wc, [temp_file.name])

            self.assertEqual(result.exit_code, 0)
            self.assertEqual(result.output, "  2\t7\t32\t" + temp_file.name + "\n")

    # def test_wc_without_file(self):
    #     runner = CliRunner()
    #     result = runner.invoke(wc, [])

    #     self.assertEqual(result.exit_code, 0)
    #     self.assertEqual(result.output, "  0\t0\t0\n")

    def test_wc_with_multiple_files(self):
        # Create two temporary files with known content for testing
        with tempfile.NamedTemporaryFile(
            mode="w+"
        ) as temp_file1, tempfile.NamedTemporaryFile(mode="w+") as temp_file2:

            temp_file1.write("Hello World!\nThis is a test.")
            temp_file1.seek(0)

            temp_file2.write("Another test file.")
            temp_file2.seek(0)

            runner = CliRunner()
            result = runner.invoke(wc, [temp_file1.name, temp_file2.name])

            self.assertEqual(result.exit_code, 0)
            expected_output = f"  2\t7\t32\t{temp_file1.name}\n  1\t4\t20\t{temp_file2.name}\n  3\t11\t52\ttotal\n"
            self.assertEqual(result.output, expected_output)


if __name__ == "__main__":
    unittest.main()
