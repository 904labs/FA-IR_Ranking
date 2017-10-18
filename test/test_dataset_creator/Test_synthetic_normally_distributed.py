'''
Created on Oct 9, 2017

@author: meike.zehlike
'''
import unittest
import numpy as np
from dataset_creator import synthetic_normally_distributed

class Test(unittest.TestCase):


    def test_create(self):
        data = synthetic_normally_distributed.create_multinomial(2, 0, 0)
        self.assertEqual(2, len(data))
        for data_points in data.values():
            self.assertAlmostEqual(0, np.mean(data_points), delta=5)

        data = synthetic_normally_distributed.create_multinomial(2, 50, 0)
        self.assertEqual(2, len(data))
        self.assertAlmostEqual(0, np.mean(data[0]), delta=5)
        self.assertAlmostEqual(50, np.mean(data[1]), delta=5)

        data = synthetic_normally_distributed.create_multinomial(2, 50, 100)
        self.assertEqual(2, len(data))
        self.assertAlmostEqual(0, np.mean(data[0]), delta=5)
        self.assertAlmostEqual(50, np.mean(data[1]), delta=5)
        self.assertAlmostEqual(100, np.std(data[0]), delta=5)
        self.assertAlmostEqual(200, np.std(data[1]), delta=5)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()