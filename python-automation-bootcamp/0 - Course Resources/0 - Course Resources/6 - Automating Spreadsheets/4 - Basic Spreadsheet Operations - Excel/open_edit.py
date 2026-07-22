import openpyxl

wb = openpyxl.load_workbook('my_workbook.xlsx')

ws = wb.active

ws['A1'] = 'Hello Excel!'

wb.save('my_workbook.xlsx')