import unittest
import wINT
import wFLOAT


class Tests(unittest.TestCase):
    def test_wInt(self):
        # ADD
        self.assertEqual(wINT.weirdINT(10) + '5', wINT.weirdINT(15))
        self.assertEqual(wINT.weirdINT(10) + '5.9', wINT.weirdINT(15))
        self.assertEqual(wINT.weirdINT(10) + 5.9, wINT.weirdINT(15))
        self.assertEqual(wINT.weirdINT(10) + 5, wINT.weirdINT(15))
        self.assertEqual(wINT.weirdINT(10) + wFLOAT.weirdFLOAT(5.9), wINT.weirdINT(15))
        self.assertEqual(wINT.weirdINT(10) + wINT.weirdINT(5), wINT.weirdINT(15))
        # SUB
        self.assertEqual(wINT.weirdINT(10) - '5', wINT.weirdINT(5))
        self.assertEqual(wINT.weirdINT(10) - '5.9', wINT.weirdINT(5))
        self.assertEqual(wINT.weirdINT(10) - 5.9, wINT.weirdINT(5))
        self.assertEqual(wINT.weirdINT(10) - 5, wINT.weirdINT(5))
        self.assertEqual(wINT.weirdINT(10) - wFLOAT.weirdFLOAT(5.9), wINT.weirdINT(5))
        self.assertEqual(wINT.weirdINT(10) - wINT.weirdINT(5), wINT.weirdINT(5))

    def test_wFloat(self):
        # ADD
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) + '1.2', wFLOAT.weirdFLOAT(2.61))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) + '1', wFLOAT.weirdFLOAT(2.41))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) + 1.2, wFLOAT.weirdFLOAT(2.61))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) + 1, wFLOAT.weirdFLOAT(2.41))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) + wFLOAT.weirdFLOAT(1.2), wFLOAT.weirdFLOAT(2.61))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) + wINT.weirdINT(1), wFLOAT.weirdFLOAT(2.41))
        # SUB
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) - '1.2', wFLOAT.weirdFLOAT(0.21))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) - '1', wFLOAT.weirdFLOAT(0.41))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) - 1.2, wFLOAT.weirdFLOAT(0.21))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) - 1, wFLOAT.weirdFLOAT(0.41))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) - wFLOAT.weirdFLOAT(1.2), wFLOAT.weirdFLOAT(0.21))
        self.assertEqual(wFLOAT.weirdFLOAT(1.41) - wINT.weirdINT(1), wFLOAT.weirdFLOAT(0.41))

if __name__ == '__main__':
    unittest.main()
