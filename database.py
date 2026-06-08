import sqlite3

def create_database():
    conn = sqlite3.connect('emails.db')
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    
    conn.commit()
   
    
    
def add_email(name,email):
    email = email.strip().lower()
    name = name.strip().lower()
    if not email:
        return False, "Email can't be empty!"
    try:
        with sqlite3.connect('emails.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           INSERT INTO users (name,email) values(?,?)
                           """,(name, email))
        return True, f"{email} added successfully"
    except sqlite3.IntegrityError:
        return False, f"{email} already exists in the database!"
    
def get_all_emails():
    with sqlite3.connect('emails.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM users ORDER BY id DESC")
        return [row[0] for row in cursor.fetchall()]
    
    
def delete_email(email):
    """Deletes an email from the database."""
    try:
        with sqlite3.connect("emails.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE email = ?", (email,))
            conn.commit()
        return True, f"'{email}' has been removed."
    except Exception as e:
        return False, f"Error deleting email: {str(e)}"