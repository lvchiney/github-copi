import unittest
from password_validator import password_validator

class TestPasswordValidator(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(password_validator("Valid1@Password"))

    def test_no_uppercase(self):
        with self.assertRaises(ValueError):
            password_validator("invalid1@password")

    def test_no_digit(self):
        with self.assertRaises(ValueError):
            password_validator("Invalid@Password")

    def test_no_special_char(self):
        with self.assertRaises(ValueError):
            password_validator("Invalid1Password")

    def test_too_short(self):
        with self.assertRaises(ValueError):
            password_validator("V1@p")

    def test_no_lowercase(self):
        with self.assertRaises(ValueError):
            password_validator("INVALID1@PASSWORD")

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPasswordValidator)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(f"\nNumber of test cases run: {result.testsRun}")
    print(f"Number of test cases passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Number of test cases failed: {len(result.failures) + len(result.errors)}")