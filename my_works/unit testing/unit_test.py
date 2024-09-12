import unittest
from io import StringIO
from main import adder
import sys

class TestMyProg(unittest.TestCase):
    def test_input_file(self):
        test_input = "3\n5 7\n2 8\n10 12\n"
        expected_output = "12\n10\n22\n"

        sys.stdin = StringIO(test_input)
        sys.stdout = StringIO()

        adder()

        output = sys.stdout.getvalue()

        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
