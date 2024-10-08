﻿# Write Data to Google Sheet using gspread in Python

 This project provides a simple Python script to write data to a Google Sheet using the gspread library and Google OAuth 2.0 for authentication.

# Features
1) Authenticate your Google account to access Google Sheets.
2) Write data to a specific Google Sheet and range using its URL.
3) Easily manage and update data in your Google Sheets programmatically.

# Prerequisites
1) Python 3.6 or higher.
2) A Google Cloud project with the Google Sheets API and Google Drive API enabled.
3) OAuth 2.0 credentials file (credentials.json) from the Google Cloud Console.

# Installation
1) git clone https://github.com/mudassirzeya/write_data_to_google_sheet.git
2) pip install django
3) pip install gspread

# Note
  I have not provided the credentials.json file. You can obtain it from Google Cloud Console by enabling the Google Drive API and Google Sheets API, and then creating the credentials.

# Usage
1) Write Data to Google Sheet
  Use the write_to_google_sheet function to write data to a Google Sheet:
  ![image](https://github.com/user-attachments/assets/524da252-6807-443d-82d4-4a61b8c521c0)
2) Customize the Data
  Modify the data_for_sheet variable to include the data you want to write to the Google Sheet. The data should be a list of lists, where each inner list represents a row of data.

# Example
  Here's a simple example of how to use the script to write data:
  ![image](https://github.com/user-attachments/assets/7e83b2ea-4b1a-4bc4-88bb-1c3162f429e4)



