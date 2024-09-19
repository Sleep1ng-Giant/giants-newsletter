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


# Define the required scopes and file paths
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CREDENTIALS_FILE = '/home/kalin/Documents/GMAIL-API-TOKEN.json'  # Path to your OAuth 2.0 credentials
TOKEN_FILE = 'token.json'  # File to store the OAuth 2.0 token

def get_credentials():
    
    creds = None
    #load credentials from path if it exists
    if os.path.exists(TOKEN_FILE):
        creds = google.oauth2.credentials.Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # If no valid credentials are available, refresh or get new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for future use
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds


def create_message(sender, to, subject, html_body):
    
    # Create a multipart email message
    message = MIMEMultipart()
    message['To'] = to
    message['From'] = sender
    message['Subject'] = subject
    
    # Attach the HTML content
    message.attach(MIMEText(html_body, 'html'))

    # Encode the message to base64
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_message(service, sender, to, subject, html_body):
    
    try:
        message = create_message(sender, to, subject, html_body)
        message = service.users().messages().send(userId="me", body=message).execute()
        print('Message Id: %s' % message['id'])
        return message
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None
    


def main():
    # Load environment variables
    load_dotenv()
    gmail_address = os.getenv("GMAIL_ADDRESS")

    # Get OAuth 2.0 credentials and build the Gmail API service
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    # Read HTML content from file
    with open('path/to/newsletter.html', 'r') as file:
        html_content = file.read()

    # Define email content
    subject = 'Your Newsletter Subject'

    # Send the email
    send_message(service, gmail_address, recipient_email, subject, html_content)

if __name__ == '__main__':
    main()