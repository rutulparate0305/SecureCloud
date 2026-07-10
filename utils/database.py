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
    
    cursor.execute(""" 
          CREATE TABLE IF NOT EXISTS files(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   owner TEXT NOT NULL,
                   original_name TEXT NOT NULL,
                   stored_name TEXT NOT NULL,
                   file_size INTEGER NOT NULL,
                   uploaded_at TEXT NOT NULL,
                   checksum TEXT NOT NULL,
                   status TEXT NOT NULL   
                   )
     """)
    
    cursor.execute(""" 
          CREATE TABLE IF NOT EXISTS user_keys(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   encryption_key TEXT NOT NULL,
                   FOREIGN KEY (username) REFERENCES user (username)
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


def add_file_metadata(owner,
                      original_name,
                      stored_name,
                      file_size,
                      uploaded_at,
                      checksum,
                      status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
      INSERT INTO files
        (owner, original_name, stored_name, file_size, uploaded_at, checksum, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,(
      owner,
      original_name,
      stored_name,
      file_size,
      uploaded_at,
      checksum,
      status
    ))

    conn.commit()
    conn.close()

def delete_file_metadata(stored_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
      DELETE FROM files
      WHERE stored_name = ?
    """,(stored_name,))

    conn.commit()
    conn.close()

def update_file_status(stored_name, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
       UPDATE files 
       SET status = ?
       WHERE stored_name = ?
    """,(status,stored_name))

    conn.commit()
    conn.close()

def get_user_files(owner):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
       SELECT original_name,
            stored_name,
            file_size,
            uploaded_at,
            checksum,
            status
       FROM files 
       WHERE owner= ?
    """,(owner,))
    files = cursor.fetchall()

    conn.close()
    return files
    
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

def save_user_key(username, encryption_key):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            INSERT INTO user_keys(username, encryption_key)
            VALUES (?,?)
""",(username,encryption_key))
    
    conn.commit()
    conn.close()

def get_user_key(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(""" 
           SELECT encryption_key
            FROM user_keys
            WHERE username = ?
""",(username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    return None
