import unittest

class TestExercise(unittest.TestCase):
    def test_assertion(self):
        value = 'XYZ'
        self.assertEqual('xyz', value.lower())

if __name__ == "__main__":
    unittest.main()