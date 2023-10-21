import sqlite3

def setup_database():
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients 
                 (name TEXT, owe_amount REAL, last_activity TEXT, booked_activity TEXT)''')
    conn.commit()
    conn.close()

def add_client(name, owe_amount, last_activity, booked_activity):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    c.execute("INSERT INTO clients (name, owe_amount, last_activity, booked_activity) VALUES (?, ?, ?, ?)", 
              (name, owe_amount, last_activity, booked_activity))

    conn.commit()
    conn.close()

def get_client_info(face_name):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clients WHERE name=?", (face_name,))
    data = c.fetchone()
    conn.close()
    if data:
        return {
            "name": data[0],
            "owe_amount": data[1],
            "last_activity": data[2],
            "booked_activity": data[3]
        }
    else:
        return None
