import unittest
from password_generator.generator import generate_password
from password_generator.strength_checker import check_strength

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_default(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_strength_checker(self):
        strong_password = "A1b@3456"
        self.assertEqual(check_strength(strong_password), "Strong")

if __name__ == "__main__":
    unittest.main()
