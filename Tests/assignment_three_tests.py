import unittest
import assignment_three



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
        assert(72)


if __name__ == '__main__':
    unittest.main()

