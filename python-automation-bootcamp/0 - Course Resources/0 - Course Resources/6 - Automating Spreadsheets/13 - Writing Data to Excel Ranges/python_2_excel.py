import openpyxl

data = [
    ["Product", "Category", "Price"],
    ["Apple iPhone 12", "Electronics", 799],
    ["Nike Air Force 1", "Footwear", 90],
    ["The Alchemist", "Books", 16.99],
    ["Instant Pot Duo", "Home & Kitchen", 89]
]

wb = openpyxl.load_workbook('Python 2 Excel.xlsx')

ws = wb['Sheet1']

rng_addr = 'A1:C' + str(len(data))

rng = ws[rng_addr]

for i in range(len(data)):
    row = data[i]

    for j in range(len(row)):
        val = row[j]

        rng[i][j].value = val

wb.save('Python 2 Excel.xlsx')
