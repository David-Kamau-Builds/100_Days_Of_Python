import datetime
import uuid
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)

def send_email(name, email, message, confirmation_id):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"New Contact Form Message - {confirmation_id}"
    
    body = f"""New message received:

Name: {name}
Email: {email}
Confirmation ID: {confirmation_id}

Message:
{message}"""
    
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

@app.route('/')
def index():
    year = datetime.datetime.now().year
    return render_template('index.html', year=year)

@app.route('/submit', methods=['POST'])
def receive_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    confirmation_id = str(uuid.uuid4())[:8].upper()
    timestamp = datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')
    current_year = datetime.datetime.now().year
    
    send_email(name, email, message, confirmation_id)
    
    return render_template('message.html', 
                         name=name, 
                         email=email, 
                         message=message,
                         confirmation_id=confirmation_id,
                         timestamp=timestamp,
                         current_year=current_year)



if __name__ == '__main__':
    app.run(debug=True)