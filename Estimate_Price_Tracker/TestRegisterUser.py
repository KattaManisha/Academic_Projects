import unittest
from app import register_user, connect_to_db

class TestApp(unittest.TestCase):

    def setUp(self):
        # Set up any initial configurations or resources needed for the tests
        self.conn = connect_to_db()

    def tearDown(self):
        # Clean up any resources (e.g., remove test users) after each test
        if self.conn:
            cursor = self.conn.cursor()
            try:
                cursor.execute("DELETE FROM se_project.users WHERE email = %s", ("test@example.com",))
                self.conn.commit()
            except Exception as e:
                print("Error during tearDown:", e)
            finally:
                cursor.close()

            # Re-establish the connection to the database to ensure proper cleanup
            self.conn = connect_to_db()
            if self.conn:
                self.conn.close()


            
    def test_register_user_success(self):
        # Arrange
        username = "test_user"
        first_name = "Test"
        last_name = "User"
        email = "test@example.com"
        password = "password123"

        # Act
        result = register_user(self.conn, username, first_name, last_name, email, password)

        # Assert
        self.assertTrue(result, "Registration should be successful")
        
        # Additional assertion to check if the user is actually inserted in the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM se_project.users WHERE email = %s", (email,))
        inserted_user = cursor.fetchone()
        cursor.close()
        self.assertIsNotNone(inserted_user, "User should be inserted in the database")

    def test_register_user_failure(self):
        # Arrange
        username = "Hope123"
        first_name = "Hope"
        last_name = "Andrea"
        email = "hay@gmail.com"  # Assuming this email already exists in the database
        password = "1234"

        # Act
        result = register_user(self.conn, username, first_name, last_name, email, password)
        
        # Assert
        self.assertFalse(result, "Registration should fail due to existing email")

if __name__ == "__main__":
    unittest.main()
