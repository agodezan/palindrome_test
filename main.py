from funcs import is_palindrome
import unittest

class TestIdentifyPalindromes(unittest.TestCase):
    def test_is_true(self):
        result = is_palindrome('Anita lava la tina')
        self.assertEqual(result, True)

    def test_is_false(self):
        result = is_palindrome('Me encanta programar en Java')
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
