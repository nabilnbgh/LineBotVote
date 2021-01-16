from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1hAKwQx2njQjul5gkGCg7EIui1jDjpZCd0fhRWrS8-dw'

service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API
sheet = service.spreadsheets()
#read Sheet
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="data!A1:A14").execute()

#print row,col
values = result.get('values', [])
print(values)