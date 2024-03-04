import unittest
import tempfile
import os
from io import StringIO
from unittest.mock import patch
from ..src.main import tail, tail_stdin, main


class TestTailFunction(unittest.TestCase):
    def setUp(self):
        self.test_file_content = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nLine 8\nLine 9\nLine 10\n"
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.write(self.test_file_content.encode())
        self.test_file.close()

    def tearDown(self):
        os.remove(self.test_file.name)

    def test_tail_default(self):
        result = tail(self.test_file.name)
        expected = [
            "Line 1\n",
            "Line 2\n",
            "Line 3\n",
            "Line 4\n",
            "Line 5\n",
            "Line 6\n",
            "Line 7\n",
            "Line 8\n",
            "Line 9\n",
            "Line 10\n",
        ]
        self.assertEqual(result, expected)

    def test_tail_custom_lines(self):
        result = tail(self.test_file.name, n=5)
        expected = ["Line 6\n", "Line 7\n", "Line 8\n", "Line 9\n", "Line 10\n"]
        self.assertEqual(result, expected)

    def test_tail_stdin(self):
        with patch("sys.stdin", StringIO(self.test_file_content)):
            result = tail_stdin(num_lines=3)
            expected = ["Line 10\n", "Line 9\n", "Line 8\n"]
            self.assertEqual(result, expected)


class TestMainFunction(unittest.TestCase):
    def test_main_with_file(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file.write("File Content")
            temp_file_path = temp_file.name

        with patch("sys.argv", ["script_name.py", temp_file_path]):
            with patch("click.echo") as mock_echo:
                main([])

        mock_echo.assert_called_with("File Content", nl=False)

    def test_main_with_stdin(self):
        with patch("sys.stdin", StringIO("Stdin Content")):
            with patch("click.echo") as mock_echo:
                main([])

        mock_echo.assert_called_with("Stdin Content")


if __name__ == "__main__":
    unittest.main()
