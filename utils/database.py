import sqlite3

DATABASE = "database/secure_cloud.db"

# Opening connection to the database
def get_connection():
    return sqlite3.connect(DATABASE)

# Initializing database
def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
          CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL   
                   )
     """)
    
    conn.commit()
    conn.close()

# Add a user to databse
def add_user(username,password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
      INSERT INTO users (username,password)
      VALUES (?,?)  
        """,(username,password))
    
    conn.commit()
    conn.close()

# Search for user in database
def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""  
      SELECT * FROM users 
      WHERE username = ?
     """,(username,))
    
    user = cursor.fetchone()
    
    conn.close()
    return user
