import os
import base64
import csv
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
<<<<<<< HEAD
CREDENTIALS_FILE = '/home/kalin/Documents/GMAIL-API-TOKEN.json'  # Path to your OAuth 2.0 credentials
TOKEN_FILE = 'token.json'  # File to store the OAuth 2.0 token

def get_credentials():
=======
CREDENTIALS_FILE = '/home/your/gmail/API/token.json'  # Path to your OAuth 2.0 credentials
TOKEN_FILE = 'token.json'  # File to store the OAuth 2.0 token

def get_credentials():
    """
    Load or refresh OAuth 2.0 credentials for accessing the Gmail API.

    If valid credentials exist in the token file, they are loaded. Otherwise, the function either
    refreshes expired credentials using a refresh token or initiates the OAuth flow to get new credentials.
    The credentials are then saved to the token file for future use.

    Returns:
        google.oauth2.credentials.Credentials: The credentials object used for authenticating API requests.
    """
>>>>>>> 2128406 (Added docstrings)
    
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
<<<<<<< HEAD
=======
    """
    Create an email message in MIME format, encoding the content in base64.

    This function constructs a MIME email with HTML content, encodes it in base64, and prepares it for
    sending via the Gmail API.

    Args:
        sender (str): The email address of the sender.
        to (str): The recipient email address.
        subject (str): The subject of the email.
        html_body (str): The HTML content to be included in the email body.

    Returns:
        dict: A dictionary containing the base64-encoded raw message, ready to be sent via the Gmail API.
    """
>>>>>>> 2128406 (Added docstrings)
    
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
<<<<<<< HEAD
=======
    """
    Send an email message using the Gmail API.

    This function sends an email created with the `create_message` function via the Gmail API.
    It catches any HTTP errors that occur during the API call and prints relevant error information.

    Args:
        service (googleapiclient.discovery.Resource): The Gmail API service object, authenticated via OAuth 2.0.
        sender (str): The email address of the sender.
        to (str): The recipient email address.
        subject (str): The subject of the email.
        html_body (str): The HTML content to be included in the email body.

    Returns:
        dict: The response from the Gmail API, containing details of the sent message.
        None: If an error occurs during the message sending.
    """
>>>>>>> 2128406 (Added docstrings)
    
    try:
        message = create_message(sender, to, subject, html_body)
        message = service.users().messages().send(userId="me", body=message).execute()
        print('Message Id: %s' % message['id'])
        return message
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None
    
def read_recipients_from_csv(file_path):
<<<<<<< HEAD
=======
    """
    Reads recipient information from a CSV file and returns a list of tuples containing names and email addresses.
    
    The CSV file is expected to have columns labeled 'name' and 'email'. Each row in the file represents a recipient,
    where the 'name' column contains the recipient's name, and the 'email' column contains their email address.
    
    Args:
        file_path (str): The path to the CSV file to read.
        
    Returns:
        list of tuple: A list of tuples, where each tuple contains two elements:
            - name (str): The name of the recipient.
            - email (str): The email address of the recipient.
    
    Example:
        Given a CSV file with the following content:
            name,email
            John Doe,john.doe@example.com
            Jane Smith,jane.smith@example.com

        The function would return:
            [('John Doe', 'john.doe@example.com'), ('Jane Smith', 'jane.smith@example.com')]
    """
    
>>>>>>> 2128406 (Added docstrings)
    recipients = []
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipients.append((row['name'], row['email']))
    return recipients

def main():
<<<<<<< HEAD
=======
    """
    Main function to send emails to a list of recipients.

    This function loads environment variables, authenticates the Gmail API using OAuth 2.0 credentials,
    reads HTML content from a file, and sends an email to each recipient listed in a CSV file.

    Workflow:
    1. Loads Gmail credentials and authenticates the Gmail API.
    2. Reads email content (HTML) from a file.
    3. Reads a list of recipients from a CSV file, which includes names and email addresses.
    4. Sends an email to each recipient using the Gmail API.

    The CSV file should contain two columns: 'name' (recipient's name) and 'email' (recipient's email address).
    The HTML file contains the body of the email, and the subject is defined within the function.

    Environment Variables:
        GMAIL_ADDRESS (str): The Gmail address from which emails will be sent. This is loaded from a `.env` file.

    Example Usage:
        Run this script from the command line to send bulk emails to recipients listed in a CSV file.
    """
    
>>>>>>> 2128406 (Added docstrings)
    # Load environment variables
    load_dotenv()
    gmail_address = os.getenv("GMAIL_ADDRESS")

    # Get OAuth 2.0 credentials and build the Gmail API service
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    # Read HTML content from file
<<<<<<< HEAD
    with open('test.html', 'r') as file:
        html_content = file.read()

    # Define email content
    subject = 'Your Newsletter Subject'

    # Read recipients from CSV
    recipients = read_recipients_from_csv('subscribers.csv')
=======
    with open('your-file-here.html', 'r') as file:
        html_content = file.read()

    # Define email content
    subject = 'Enter your subject line here'

    # Read recipients from CSV
    recipients = read_recipients_from_csv('list-of-your-subscribers.csv')
>>>>>>> 2128406 (Added docstrings)
    
    for name, email in recipients:
        print(f'Sending email to {name} <{email}>...')
        send_message(service, gmail_address, email, subject, html_content)

if __name__ == '__main__':
    main()