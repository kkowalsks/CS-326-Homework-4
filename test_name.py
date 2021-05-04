import unittest
import name

class testCaseName(unittest.TestCase):
    def test_fullname(self):
        self.assertEqual(name.fullname("John", "Smith"), "John Smith")
        self.assertEqual(name.fullname("123", "321"), "123 321")
        self.assertEqual(name.fullname("lorem", "ipsum"), "loremipsum")



if __name__ == '__main__':
    unittest.main()