import unittest
from app import login_user, connect_to_db

class TestApp(unittest.TestCase):

    def test_login_user_success(self):
        # Arrange
        conn = connect_to_db()
        if conn:
            email = "hope@gmail.com"
            password = "1234"

            # Assuming this user is registered with the given email and password
            # You may want to create a test user in the database for testing

            # Act
            result = login_user(email, password)

            # Assert
            self.assertTrue(result)
        

    def test_login_user_failure(self):
        # Arrange
        conn = connect_to_db()
        # Provide invalid data, e.g., incorrect password
        email = "hope@gmail.com"
        password = "12345"

        # Act
        result = login_user(email, password)

        # Assert
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
