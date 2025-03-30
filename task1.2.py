import unittest
from unittest.mock import patch

def process_input():
    user_input = input("Enter something: ")
    return f"You entered: {user_input}"

class TestProcessInput(unittest.TestCase):
    @patch("builtins.input", return_value="test")
    def test_process_input(self, mock_input):
        result = process_input()
        self.assertEqual(result, "You entered: test")

if __name__ == "__main__":
    unittest.main()
