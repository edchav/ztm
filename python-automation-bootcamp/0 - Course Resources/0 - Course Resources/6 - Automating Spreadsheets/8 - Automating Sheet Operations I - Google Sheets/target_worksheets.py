import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open('gspread 101')

active_ws = spreadsheet.sheet1

print(active_ws.title)

ws = spreadsheet.worksheet('Sheet2')
ws.update_title('Second Sheet')