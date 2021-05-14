import wordcount
import unittest

class testCaseWordCount(unittest.TestCase):
    def test_wordcount(self):
        print(" === testing wordcounts ")
        print( " testing 'i am homeless' ")

        text = "i am homeless"
        num = wordcount.wordCount(text)
        self.assertEqual(num, 3)

        print( " testing ' i think i need to do something about my test cases'")
        text = "i think i need to do something about my test cases"
        num = wordcount.wordCount(text)
        self.assertEqual(num, 11)

        print( " testing: 0 0 0 0 0 0 0 0 0 0 0 0 ")
        text = "0 0 0 0 0 0 0 0 0 0 0 0"
        num = wordcount.wordCount(text)
        self.assertEqual(num, 12)

        print( " testing: ' '")
        text = " "
        num = wordcount.wordCount(text)
        self.assertEqual(num, 0)

if __name__ == '__main__':
    unittest.main()