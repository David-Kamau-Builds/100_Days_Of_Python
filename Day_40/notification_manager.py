import smtplib
import os
from twilio.rest import Client

class NotificationManager:

    def __init__(self):
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.twilio_virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self.twilio_verified_number = os.environ["TWILIO_VERIFIED_NUMBER"]
        self.whatsapp_number = os.environ["TWILIO_WHATSAPP_NUMBER"]
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        try:
            message = self.client.messages.create(
                from_=self.twilio_virtual_number,
                body=message_body,
                to=self.twilio_verified_number
            )
            print(f"SMS sent: {message.sid}")
        except Exception as e:
            print(f"Error sending SMS: {e}")

    def send_whatsapp(self, message_body):
        try:
            message = self.client.messages.create(
                from_=f'whatsapp:{self.whatsapp_number}',
                body=message_body,
                to=f'whatsapp:{self.twilio_verified_number}'
            )
            print(f"WhatsApp sent: {message.sid}")
        except Exception as e:
            print(f"Error sending WhatsApp: {e}")

    def send_emails(self, email_list, email_body):
        try:
            with smtplib.SMTP(self.smtp_address) as connection:
                connection.starttls()
                connection.login(self.email, self.email_password)
                for email in email_list:
                    connection.sendmail(
                        from_addr=self.email,
                        to_addrs=email,
                        msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                    )
            print(f"Emails sent to {len(email_list)} recipients")
        except Exception as e:
            print(f"Error sending emails: {e}")