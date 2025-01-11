import unittest

class TestExercise(unittest.TestCase):
    def test_assertion(self):
        lst = ['xyz']
        self.assertIn('xyz', lst)

if __name__ == "__main__":
    unittest.main()