import unittest

class TestExercise(unittest.TestCase):
    def test_assertion(self):
        value = None
        self.assertIsNone(value)

if __name__ == "__main__":
    unittest.main()