import openpyxl

wb = openpyxl.load_workbook('Automating Worksheets.xlsx')

active_ws = wb.active

print(active_ws.title)

ws = wb['Sheet3']
ws.title = 'Third Sheet'

wb.save('Automating Worksheets.xlsx')