import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import google.auth.transport.requests
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load secrets from .env
load_dotenv()
gmail_address = os.getenv("GMAIL_ADDRESS")
gmail_password = os.getenv("GMAIL_PASSWORD")

# Define the required scopes and file paths
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CREDENTIALS_FILE = '/home/kalin/Documents/GMAIL-API-TOKEN.json'  # Path to your OAuth 2.0 credentials
TOKEN_FILE = 'token.json'  # File to store the OAuth 2.0 token

#Create the email
email = EmailMessage()

# Subject line of the email
email["Subject"] = "Automated newsletter with Python & Github Actions"
# Sender of the email
email["From"] = gmail_address

# Add HTML content to the email
email.add_alternative(f"""\
<html>
<head></head>
<body>
    <p>Brought to you by <b>Sleep1ng-Giant</b></p>
</body>
</html>
""", subtype="html")
#TODO Add HTML file passthrough

# Add plaintext alternative as fallback option
email.add_alternative("Brought to you by Sleep1ng-Giant")

# Send the email to the newsletter subscribers
subscriber_email_addresses = ['']
#TODO add email addr file passthrough
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp_server:
    smtp_server.login(gmail_address, gmail_password)
    
    for subsciber_email_address in subscriber_email_addresses:
        # Set the recipient for the email
        email["To"] = subsciber_email_address

        smtp_server.send_message(email)