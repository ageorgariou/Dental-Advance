import smtplib
from email.message import EmailMessage
import ssl
import sqlite3

EMAIL_PASSWORD = 'feidzxooysqlhbkh'

def get_client_info(name):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clients WHERE name=?", (name,))
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

def send1_email(client_name):
    client_info = get_client_info(client_name)
    
    if not client_info:  # If no client info found for the client_name, exit the function
        print(f"No client info found for {client_name}. Email not sent.")
        return

    # Construct email details using client_info
    email_sender = 'jrcshortclips@gmail.com'
    email_recipient = 'jrcshortclips@gmail.com'  # Change this to the recipient's email address
    subject = f"Alert: {client_info['name']} detected"
    body = f"""{client_info['name']} detected!
    Owe Amount: ${client_info['owe_amount']}.
    Last Activity: {client_info['last_activity']}.
    Booked for: {client_info['booked_activity']}."""

    # Print email details
    print(f"Sending Email to: {email_recipient}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")

    try:
        # Below is your code for sending the email.
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_recipient
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, EMAIL_PASSWORD)
            smtp.sendmail(email_sender, email_recipient, em.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f"Email sending failed with error: {e}")

# Example usage:
# client_name = "Alexandros Georgariou"
# send1_email(client_name)
