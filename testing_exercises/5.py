import unittest

class TestExercise(unittest.TestCase):
    def test_assertion(self):
        lst = ['a']
        self.assertNotIn('xyz', lst)

if __name__ == "__main__":
    unittest.main()