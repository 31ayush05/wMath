import unittest
import wInt
import wFloat


class Tests(unittest.TestCase):
    def test_wInt(self):
        # ADD
        self.assertEqual(wInt.wInt(10) + '5', wInt.wInt(15))
        self.assertEqual(wInt.wInt(10) + '5.9', wInt.wInt(15))
        self.assertEqual(wInt.wInt(10) + 5.9, wInt.wInt(15))
        self.assertEqual(wInt.wInt(10) + 5, wInt.wInt(15))
        self.assertEqual(wInt.wInt(10) + wFloat.wFloat(5.9), wInt.wInt(15))
        self.assertEqual(wInt.wInt(10) + wInt.wInt(5), wInt.wInt(15))
        # SUB
        self.assertEqual(wInt.wInt(10) - '5', wInt.wInt(5))
        self.assertEqual(wInt.wInt(10) - '5.9', wInt.wInt(5))
        self.assertEqual(wInt.wInt(10) - 5.9, wInt.wInt(5))
        self.assertEqual(wInt.wInt(10) - 5, wInt.wInt(5))
        self.assertEqual(wInt.wInt(10) - wFloat.wFloat(5.9), wInt.wInt(5))
        self.assertEqual(wInt.wInt(10) - wInt.wInt(5), wInt.wInt(5))

    def test_wFloat(self):
        # ADD
        self.assertEqual(wFloat.wFloat(1.41) + '1.2', wFloat.wFloat(2.61))
        self.assertEqual(wFloat.wFloat(1.41) + '1', wFloat.wFloat(2.41))
        self.assertEqual(wFloat.wFloat(1.41) + 1.2, wFloat.wFloat(2.61))
        self.assertEqual(wFloat.wFloat(1.41) + 1, wFloat.wFloat(2.41))
        self.assertEqual(wFloat.wFloat(1.41) + wFloat.wFloat(1.2), wFloat.wFloat(2.61))
        self.assertEqual(wFloat.wFloat(1.41) + wInt.wInt(1), wFloat.wFloat(2.41))
        # SUB
        self.assertEqual(wFloat.wFloat(1.41) - '1.2', wFloat.wFloat(0.21))
        self.assertEqual(wFloat.wFloat(1.41) - '1', wFloat.wFloat(0.41))
        self.assertEqual(wFloat.wFloat(1.41) - 1.2, wFloat.wFloat(0.21))
        self.assertEqual(wFloat.wFloat(1.41) - 1, wFloat.wFloat(0.41))
        self.assertEqual(wFloat.wFloat(1.41) - wFloat.wFloat(1.2), wFloat.wFloat(0.21))
        self.assertEqual(wFloat.wFloat(1.41) - wInt.wInt(1), wFloat.wFloat(0.41))

if __name__ == '__main__':
    unittest.main()
