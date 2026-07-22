import openpyxl

wb = openpyxl.load_workbook('Employee Ratings.xlsx')

ws = wb['Ratings']

rng = ws['B2:E11']

for row in rng:
    for cell in row:
        val = cell.value

        if type(val) != int:
            cell.value = ''
        elif val < 0:
            cell.value = 0
        elif val > 10:
            cell.value = 10

wb.save('Employee Ratings.xlsx')