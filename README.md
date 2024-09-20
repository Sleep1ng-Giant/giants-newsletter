# Welcome to The Giant's Newsletter! 📬

My life has been a bit of a rollercoaster this past year, and it's been a challenge keeping all of my friends up to date. Thankfully, newsletters exist! Rather than paying for a newsletter service, I decided to create my own system that allows me to easily send personalized newsletters to everyone, and you can too! 😉

This project automates the process of sending bulk newsletters via Gmail, leveraging the Gmail API and a CSV file of recipients. It's ideal for personal use or small mailing lists, and it’s completely free to use within Gmail’s daily email limits (500 emails per day).

## Features

- Send personalized HTML-based newsletters to a list of recipients.
- Use Gmail's free tier to send up to 500 emails per day.
- Automate bulk sending without needing a paid newsletter service.
- Easily manage your recipient list via a simple CSV file.
- Authenticate with Google securely using OAuth 2.0.

---

## Prerequisites

Before you begin, you’ll need the following:

1. **Gmail account**: You’ll need a Gmail account to send the emails.
2. **Google Cloud Project**: This is necessary to use the Gmail API.
3. **Python 3.x**: Make sure you have Python installed.
4. **Google API Credentials**: You’ll need OAuth 2.0 credentials from Google to authenticate.

---

## Setup Instructions

### 1. Create a Gmail Account (or Use an Existing One)
Gmail allows you to send up to 500 emails per day for free, which is ideal for small mailing lists.

### 2. Create a Google Cloud Project and Enable the Gmail API

1. **Create a Google Cloud Project**:
   - Visit the [Google Cloud Console](https://console.cloud.google.com/), create a new project, or select an existing one.
   
2. **Enable the Gmail API**:
   - In the Cloud Console, navigate to **API Library**.
   - Search for "Gmail API" and click "Enable".

3. **Create OAuth 2.0 Credentials**:
   - Go to the **Credentials** section in the Cloud Console.
   - Click **Create Credentials** and select **OAuth 2.0 Client IDs**.
   - Choose **Desktop app** or **Web application**, depending on how you plan to use the newsletter.
   - Download the `credentials.json` file and place it in the project folder.

### 3. Install Dependencies

You’ll need the following Python packages to work with Gmail’s API and send emails. Install them via pip:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dotenv
```

These libraries will help with:
- **OAuth 2.0** authentication.
- Interacting with the **Gmail API** to send emails.
- Managing your environment variables securely.

---

## Usage Instructions

### Step 1: Set Up Your Environment Variables

You’ll need to create a `.env` file in the root of your project to store sensitive data (such as your Gmail address). Here’s an example `.env` file:

```env
GMAIL_ADDRESS=your-email@gmail.com
```

### Step 2: Prepare Your Newsletter Content

1. **HTML File**: Create a `your-file-here.html` file that contains the HTML body of your newsletter.
   
2. **CSV File**: Create a `list-of-your-subscribers.csv` file with two columns: `name` and `email`. This file will be used to personalize and send the newsletter to your recipients. Example:

    ```csv
    name,email
    John Doe,john.doe@example.com
    Jane Smith,jane.smith@example.com
    ```

### Step 3: Run the Script

To send the newsletter, simply run the `main.py` script:

```bash
python main.py
```

This will:
- Load your Gmail credentials.
- Read the HTML file for the email body.
- Send personalized emails to each recipient listed in your CSV file.

---

## Project Structure

```
├── .env                     # Environment variables (Gmail address)
├── credentials.json          # Google API OAuth 2.0 credentials
├── list-of-your-subscribers.csv # List of recipients
├── your-file-here.html       # HTML content for the newsletter
├── newsletter.py                   # Main script to send the newsletter
├── README.md                 # Project documentation
```

---

## Known Limitations

- **Gmail Send Limits**: Gmail restricts sending to 500 emails per day. If you need to send more, consider using a paid email service like SendGrid.
- **OAuth Token Expiration**: The OAuth token expires after a while, so you may need to refresh it periodically.

---

## Contributing

If you’d like to contribute to this project, feel free to fork the repository and create a pull request. Any contributions, suggestions, or improvements are welcome!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

