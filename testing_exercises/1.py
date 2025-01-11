import unittest

class TestExercise(unittest.TestCase):
    def test_assertion(self):
        value = 4
        self.assertTrue(value % 2 == 0, 'value is not odd')

if __name__ == "__main__":
    unittest.main()