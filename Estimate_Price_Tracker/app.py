from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from PriceComparison.price_comparison import get_product_price_amazon, get_product_price_ebay

app = Flask(__name__)
app.secret_key = b'\x98t\xc9\x88N\xc6\xd1\xa9\xb2\xbdK\x91\x00\xfa\xbc\xd3\x84\xd6\x89\x9dwe\x13I'

# Access the secret key from the app context
secret_key = app.config['SECRET_KEY']
print(secret_key)

# Function to establish a database connection
def connect_to_db():
    try:
        conn = psycopg2.connect(
            database="manishak",
            user="manishak",
            password="j*hp6y6dSy",
            host="db.cecs.pdx.edu",
            port="5432"
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to the database:", error)
        return None

# Function to create the "users" table in the database
def create_users_table(conn):
    try:
        cursor = conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while creating the table:", error)

def email_exists(conn, email):
    try:
        cursor = conn.cursor()
        check_email_query = "SELECT * FROM se_project.users WHERE email = %s"
        cursor.execute(check_email_query, (email,))
        existing_email = cursor.fetchone()
        return existing_email is not None
    except (Exception, psycopg2.Error) as error:
        print("Error while checking if email exists:", error)
        return False

# Function to register a new user
def register_user(conn, username, first_name, last_name, email, password):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            
             # Check if the email already exists
            if email_exists(conn, email):
                return False  # Email already exists, registration failed

            # Define the query and its parameters
            insert_user_query = """
                INSERT INTO se_project.users (username, first_name, last_name, email, password)
                VALUES (%s, %s, %s, %s, %s)
            """
            query_params = (username, first_name, last_name, email, password)

            # Execute the query
            cursor.execute(insert_user_query, query_params)

            conn.commit()
            cursor.close()
            return True
        except (Exception, psycopg2.Error) as error:
            print("Error while registering the user:", error)
        finally:
            conn.close()
    return False

def user_exists(conn, username):
    try:
        cursor = conn.cursor()
        check_user_query = "SELECT * FROM se_project.users WHERE username = %s"
        cursor.execute(check_user_query, (username,))
        existing_user = cursor.fetchone()
        return existing_user is not None
    except (Exception, psycopg2.Error) as error:
        print("Error while checking if user exists:", error)
        return False

# Function to update user-info
def update_user(conn, username, first_name, last_name, email):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            
             # Check if the user already exists
             
            if user_exists(conn, username):
                return False  # user already exists

            # Define the query and its parameters
            update_user_query = """
                UPDATE se_project.users
                SET
                  username= %s,
                  first_name= %s,
                  last_name=%s
                WHERE
                  email=%s;
            """
            query_params = (username, first_name, last_name, email)

            # Execute the query
            cursor.execute(update_user_query, query_params)

            conn.commit()
            cursor.close()
            return True
        except (Exception, psycopg2.Error) as error:
            print("Error while updating the user:", error)
        finally:
            conn.close()
    return False

# Function to handle user login
def login_user(email, password):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            # Query the database to get the stored password
            get_password_query = "SELECT password FROM se_project.users WHERE email = %s"
            cursor.execute(get_password_query, (email,))
            stored_password = cursor.fetchone()

            if stored_password and password == stored_password[0]:
                return True
        except (Exception, psycopg2.Error) as error:
            print("Error while handling user login:", error)
        finally:
            conn.close()
    return False

# Function to fetch user data from the database
def get_user_from_database(email):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()

            # Query the database to get user data by email
            get_user_query = "SELECT username, first_name, last_name, email FROM se_project.users WHERE email = %s"
            cursor.execute(get_user_query, (email,))
            user_data = cursor.fetchone()

            if user_data:
                user = {
                    'username': user_data[0],
                    'first_name': user_data[1],
                    'last_name': user_data[2],
                    'email': user_data[3]
                }
                return user
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching user data from the database:", error)
        finally:
            conn.close()
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        conn = connect_to_db()

        if conn:
            if register_user(conn, username, first_name, last_name, email, password):
                return redirect(url_for('user_home')) # Return a success response with HTTP status 200
            else:
                return "Registration failed", 400  # Return a failure response with HTTP status 400
        else:
            return "Database connection error", 500  # Return an error response if there's a database connection issue

    return "Invalid request method", 405  # Return an error response for other HTTP methods

# Handle other HTTP methods gracefully by returning an error response.

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if login_user(email, password):
            session['email'] = email  # Store the email in the session upon successful login
            return redirect(url_for('user_home'))  # Redirect to the user profile page
        else:
            return "Invalid login"
    elif request.method == 'GET':
        return "Method Not Allowed", 405

@app.route('/user-home')
def user_home():
    #Rendering User's home page
    return render_template('user_home.html')

@app.route('/fetch-home')
def fetch_home():
    #Rendering User's home page
    return render_template('fetch_home.html')

@app.route('/user_profile')
def user_profile():
    # Retrieve the email from the session if it exists
    email = session.get('email')
    
    if email:
        user = get_user_from_database(email)
        if user:
            return render_template('user_profile.html', user=user)
        else:
            return "User not found"
    else:
        return redirect(url_for('home')) 
    
@app.route('/update_user', methods=['POST'])
def update():
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email=session.get('email')
        
        conn = connect_to_db()

        if conn:
            if update_user(conn, username, first_name, last_name, email ):
                return redirect(url_for('user_profile'))
            else:
                return "updation failed"    #Return a failure response
            
@app.route('/electronics')
def electronics():
    #Rendering electronics page
    return render_template('electronics.html')

@app.route('/clothing')
def clothing():
    #Rendering clothing page
    return render_template('clothing.html')

@app.route('/watches')
def watches():
    #Rendering watches page
    return render_template('watches.html')

@app.route('/logout')
def logout():
    # Perform logout actions, e.g., clear the session
    session.clear()
    # Redirect the user to the home page or login page
    return redirect(url_for('home'))

@app.route('/compare_prices', methods=['GET'])
def compare_prices():
    amazon_url = request.args.get('amazon_url')
    ebay_url = request.args.get('ebay_url')
    
    amazon_web_url, amazon_product_price = get_product_price_amazon(amazon_url)
    ebay_web_url, ebay_product_price = get_product_price_ebay(ebay_url)

    return render_template('compare_prices.html',ebay_product_price = ebay_product_price, ebay_web_url = ebay_web_url,amazon_product_price = amazon_product_price, amazon_web_url = amazon_web_url)


if __name__ == "__main__":
    app.run(debug=True)