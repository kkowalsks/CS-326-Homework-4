import unittest
import avg_list

firstTest = []
secondTest = [1, 2, 3, 4, 5]
thirdTest = [30, 98, 18]

class testCaseFindAvg(unittest.TestCase):
    def test_findAvg(self):
        self.assertEqual(avg_list.findAvg(firstTest), 0)
        self.assertEqual(avg_list.findAvg(secondTest), 3)
        self.assertEqual(avg_list.findAvg(thirdTest), 48.666666666666)


if __name__ == '__main__':
    unittest.main()