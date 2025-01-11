import unittest

class TestExercise(unittest.TestCase):
    def test_assertion(self):
        value = 6
        self.assertIsInstance(value, Numeric)

if __name__ == "__main__":
    unittest.main()