import unittest
import mtools as mt




class testMain(unittest.TestCase):
    def test_sumatiion_func(self):
        self.assertEqual(mt.sum_apples(2,3),5)



if __name__ == "__main__":
    unittest.main()