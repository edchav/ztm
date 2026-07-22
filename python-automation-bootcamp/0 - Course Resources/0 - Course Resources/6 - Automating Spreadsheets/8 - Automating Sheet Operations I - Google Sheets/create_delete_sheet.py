import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open('gspread 101')
spreadsheet.add_worksheet(title='a new worksheet', rows=100, cols=100)

ws = spreadsheet.worksheet('Second Sheet')

spreadsheet.del_worksheet(ws)