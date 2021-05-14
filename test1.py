import test
import random
import unittest

class testCasePalindrome(unittest.TestCase):
    def test_palindrome(self):
        print(" === testing cases ")
        print("testing racecar")

        text = "racecar"
        status = test.palindrome(text)
        self.assertEqual(status, True)

        print(" testing chicken ")
        text = "chicken"
        status = test.palindrome(text)
        self.assertEqual(status, False)          # In this case, "chicken" is not a palindrome. It gave back a failed test.

        print( " testing 888 ")
        text = "888"
        status = test.palindrome(text)
        self.assertEqual(status, True)

        print( "testing '  ' ")
        text = " "
        status = test.palindrome(text)
        self.assertEqual(status, True)          # This case, we have nothing, and the case failed because it was unable to match nothing with nothing.

if __name__ == '__main__':
    unittest.main()
