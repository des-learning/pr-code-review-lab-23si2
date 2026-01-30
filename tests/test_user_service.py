import unittest
from user_service import register_user

class TestUserService(unittest.TestCase):
    
    def test_register(self):
        result = register_user("user12", "user123@")
        # Using assertEqual to compare the result
        self.assertEqual(result, "User registered successfully", f"Expected 'User registered successfully', got {result}")

if __name__ == "__main__":
    unittest.main()
