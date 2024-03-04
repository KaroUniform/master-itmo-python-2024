import unittest
from click.testing import CliRunner
from ..src.main import number_lines

class TestNumberLinesScript(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_single_file(self):
        """
        Тестирование пронумерованных строк в одном файле.
        """
        result = self.runner.invoke(number_lines, ['task-1-nl/tests/simple_input.txt'])
        self.assertEqual(result.exit_code, 0)
        expected_output = '1\tTest line 1\n2\tTest line 2'
        self.assertEqual(result.output, expected_output)

    def test_nonexistent_file(self):
        """
        Тестирование обработки ошибки при указании несуществующего файла.
        """
        result = self.runner.invoke(number_lines, ['nonexistent_file.txt'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Invalid value", result.output)

    def test_stdin(self):
        """
        Тестирование строк из stdin.
        """
        result = self.runner.invoke(number_lines, input='Test line 1\nTest line 2\n')
        self.assertEqual(result.exit_code, 0)
        expected_output = '1\tTest line 1\n2\tTest line 2\n'
        self.assertEqual(result.output, expected_output)

    def test_empty(self):
        """
        Тестирование обработки пустого файла.
        """
        result = self.runner.invoke(number_lines, ['task-1-nl/tests/empty.txt'])
        self.assertEqual(result.exit_code, 0)
        expected_output = ''
        self.assertEqual(result.output, expected_output)

if __name__ == '__main__':
    unittest.main()
