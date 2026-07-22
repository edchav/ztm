import gspread

gc = gspread.service_account('service_account_credentials.json')

new_spreadsheet = gc.create('gspread 201')

new_spreadsheet.share('tlcuzick@gmail.com', perm_type='user', role='writer')