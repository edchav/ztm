import openpyxl

wb = openpyxl.load_workbook('Employees.xlsx.xlsx')

names = ['John Smith', 'Amit Patel', 'Robert Brown', 'Sanaa Al Farsi', 'Michael Miller', 'Chiamaka Mbah', 'James Wilson', 'Maria Rodriguez', 'David Clark', 'Chen Wei']

for name in names:
    wb.create_sheet(name)

wb.save('Employees.xlsx')