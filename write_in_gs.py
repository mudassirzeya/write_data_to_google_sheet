from google.oauth2.credentials import Credentials
import gspread
from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Google Sheets API token obtained from Google Sign-In
GS_TOKEN = {"token": "Your Token Which You got from Google Sign in"}

# Define the scope for Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive']


def authenticate_google_account_for_spreadsheet():
    """
    Authenticate the user's Google account to access Google Sheets.
    This function initiates a local server for OAuth 2.0 authorization
    and generates a token that can be used to access Google Sheets.

    Returns:
        Credentials object containing the authenticated user's access token.
    """
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    token = flow.run_local_server(port=8001)
    return token


def write_to_google_sheet(template_url, sheet_name, cell_range, data):
    """
    Write data to a specific range in a Google Sheet.

    Args:
        template_url (str): The URL of the Google Sheet to be accessed.
        sheet_name (str): The name of the worksheet where data will be written.
        cell_range (str): The cell range in A1 notation where data will be written.
        data (list of lists): The data to write to the specified cell range.

    Returns:
        None
    """
    try:
        # Retrieve the existing Google Sheets API token
        gs_token = GS_TOKEN

        # Convert the token into credentials
        creds = Credentials.from_authorized_user_info(gs_token)

        # Authorize the gspread client with the obtained credentials
        gc = gspread.authorize(creds)

        # Open the Google Sheet by its URL
        sh = gc.open_by_url(template_url)

        # Select the worksheet by its name
        worksheet = sh.worksheet(sheet_name)

        # Write data to the specified cell range in the worksheet
        worksheet.update(cell_range, data)
        print("Data written successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
g_sheet_url = "Your Google Sheet Url"
data_for_sheet = [
    ['this_audit_framework.question_1', 'question_1'],
    ['this_audit_framework.question_2', 'question_2'],
    ['this_audit_framework.question_3', 'question_3'],
    ['this_audit_framework.question_4', 'question_4'],
    ['this_audit_framework.question_5', 'question_5']
]
write_to_google_sheet(g_sheet_url, 'Audit Details', 'B9:C13', data_for_sheet)
