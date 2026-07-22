import openpyxl

wb = openpyxl.load_workbook('Automating Worksheets.xlsx')

wb.create_sheet('new_sheet')

del wb['Third Sheet']

wb.save('Automating Worksheets.xlsx')