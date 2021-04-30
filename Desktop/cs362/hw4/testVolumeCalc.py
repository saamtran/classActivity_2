import unittest
import volumeCalc
import math

class testCaseVolume(unittest.TestCase):
    def test_volume(self):
        result = volumeCalc.calc(10, 9, 8)
        self.assertEqual(result, 720)

        result = volumeCalc.calc(-9,8,7)
        self.assertEqual(result, -504)

        result = volumeCalc.calc(0,12,14)
        self.assertEqual(result, 0)
        
if __name__ == '__main__':
    unittest.main()