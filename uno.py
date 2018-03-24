import unittest

class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEquals(1,1.0)


if __name__ == "__main__":
    unittest.main()
