import gspread
import re

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open_by_key('1bqccoz6XTmQGKMfwvHggPzmnyT9Hi2Emwjx2yFqDLKs')

pattern = r'^Sheet\d+$'

all_ws = spreadsheet.worksheets()

for ws in all_ws:
    if re.search(pattern, ws.title) is not None:
        spreadsheet.del_worksheet(ws)