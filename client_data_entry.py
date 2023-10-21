import tkinter as tk
import sqlite3

def create_or_update_client():
    name = name_entry.get()
    owe_amount = owe_amount_entry.get()
    last_activity = last_activity_entry.get()
    booked_activity = booked_activity_entry.get()

    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    # Check if the client already exists in the database
    c.execute("SELECT * FROM clients WHERE name=?", (name,))
    existing_client = c.fetchone()

    if existing_client:
        # If the client exists, update their information
        c.execute("UPDATE clients SET owe_amount=?, last_activity=?, booked_activity=? WHERE name=?", (owe_amount, last_activity, booked_activity, name))
    else:
        # If the client does not exist, insert a new record
        c.execute("INSERT INTO clients (name, owe_amount, last_activity, booked_activity) VALUES (?, ?, ?, ?)",
                  (name, owe_amount, last_activity, booked_activity))

    conn.commit()
    conn.close()

    # Clear input fields
    name_entry.delete(0, tk.END)
    owe_amount_entry.delete(0, tk.END)
    last_activity_entry.delete(0, tk.END)
    booked_activity_entry.delete(0, tk.END)

def edit_client():
    global name_entry, owe_amount_entry, last_activity_entry, booked_activity_entry

    name = name_entry.get()

    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    c.execute("SELECT * FROM clients WHERE name=?", (name,))
    existing_client = c.fetchone()

    if existing_client:
        owe_amount_entry.delete(0, tk.END)
        owe_amount_entry.insert(0, existing_client[1])

        last_activity_entry.delete(0, tk.END)
        last_activity_entry.insert(0, existing_client[2])

        booked_activity_entry.delete(0, tk.END)
        booked_activity_entry.insert(0, existing_client[3])

    else:
        owe_amount_entry.delete(0, tk.END)
        last_activity_entry.delete(0, tk.END)
        booked_activity_entry.delete(0, tk.END)

    conn.close()

def delete_client(client_name):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    c.execute("DELETE FROM clients WHERE name=?", (client_name,))
    conn.commit()
    conn.close()

def show_client_list():
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    c.execute("SELECT name FROM clients")
    client_names = c.fetchall()
    conn.close()

    client_list_window = tk.Toplevel(window)
    client_list_window.title("Client List")

    listbox = tk.Listbox(client_list_window)

    for client in client_names:
        listbox.insert(tk.END, client[0])

    listbox.pack()

    delete_button = tk.Button(client_list_window, text="Delete", command=lambda: delete_client(listbox.get(listbox.curselection())))
    delete_button.pack()

def main():
    global name_entry, owe_amount_entry, last_activity_entry, booked_activity_entry, window

    window = tk.Tk()
    window.title("Client Data Entry")

    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="Owe Amount").pack()
    owe_amount_entry = tk.Entry(window)
    owe_amount_entry.pack()

    tk.Label(window, text="Last Activity").pack()
    last_activity_entry = tk.Entry(window)
    last_activity_entry.pack()

    tk.Label(window, text="Booked For").pack()
    booked_activity_entry = tk.Entry(window)
    booked_activity_entry.pack()

    submit_button = tk.Button(window, text="Submit", command=create_or_update_client)
    submit_button.pack()

    edit_button = tk.Button(window, text="Edit", command=edit_client)
    edit_button.pack()

    show_list_button = tk.Button(window, text="Show Client List", command=show_client_list)
    show_list_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
