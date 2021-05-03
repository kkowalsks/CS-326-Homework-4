import unittest
import cube

class testCaseCube(unittest.TestCase):
    def test_cubic(self):
        self.assertEqual(cube.cubic(5), 125)
        self.assertGreater(cube.cubic(4.5), 50)
        self.assertEqual(cube.cubic(-5), -125)


if __name__ == "__main__":
    unittest.main()