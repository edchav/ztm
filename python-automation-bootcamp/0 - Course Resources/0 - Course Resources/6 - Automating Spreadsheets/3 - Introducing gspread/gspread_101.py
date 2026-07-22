import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open('gspread 101')
