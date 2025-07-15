import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_sheet_to_csv(sheet_url, sheet_tab, csv_output_path="input/keywords_sample.csv"):
    # Define scope and credentials
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Open the sheet and tab
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.worksheet(sheet_tab)

    # Read all records and write to CSV
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    df.to_csv(csv_output_path, index=False)

    print(f"[✅] Data pulled from Google Sheet tab '{sheet_tab}' and saved to {csv_output_path}")
