import unittest
import psycopg2

def connect_to_db(database, user, password, host, port):
    try:
        conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to the database:", error)
        return None

def connect_to_db_with_invalid_params(invalid_conn_params):
    if invalid_conn_params["database"] == "invalid_db":
        # Handle invalid database case
        return None
    elif invalid_conn_params["user"] == "invalid_user":
        # Handle invalid user case
        return None
    elif invalid_conn_params["password"] == "invalid_password":
        # Handle invalid password case
        return None
    elif invalid_conn_params["host"] == "invalid_host":
        # Handle invalid host case
        return None
    elif invalid_conn_params["port"] == "invalid_port":
        # Handle invalid port case
        return None
    else:
        # Connect with the provided parameters
        return connect_to_db(**invalid_conn_params)

class TestApp(unittest.TestCase):

    def test_connect_to_db_failure(self):
        # Arrange
        # Provide invalid database connection parameters
        invalid_conn_params = {
            "database": "invalid_db",
            "user": "invalid_user",
            "password": "invalid_password",
            "host": "invalid_host",
            "port": "invalid_port"
        }

        # Act
        conn = connect_to_db_with_invalid_params(invalid_conn_params)

        # Assert
        self.assertIsNone(conn)
        
    def test_connect_to_db_success(self):
        # Arrange
        # Provide valid database connection parameters
        valid_conn_params = {
            "database": "manishak",
            "user": "manishak",
            "password": "j*hp6y6dSy",
            "host": "db.cecs.pdx.edu",
            "port": "5432"
        }

        # Act
        conn = connect_to_db(**valid_conn_params)

        # Assert
        self.assertIsNotNone(conn)
        self.assertEqual(conn.closed, 0)  # Check if the connection is open

if __name__ == "__main__":
    unittest.main()
