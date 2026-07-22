import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open('gspread 101')

ws = spreadsheet.worksheet('Sheet1')

c = ws.acell('A1')

c_val = c.value

print(c_val)

three_val = c_val * 3

ws.update('A2', three_val)

ws.update_cell(7, 11, 'Howdy, human person!')

c_val2 = ws.cell(7, 11).value

print(c_val2)