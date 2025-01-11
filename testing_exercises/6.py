import unittest

class TestExercise(unittest.TestCase):
    def test_assertion(self):
        with self.assertRaises(NoExperienceError):
            employee.hire()

if __name__ == "__main__":
    unittest.main()