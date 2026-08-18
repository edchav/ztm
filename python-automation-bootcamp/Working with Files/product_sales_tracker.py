import csv
import datetime

data = []
with open('product_sales.txt', 'r') as file:
    lines = file.readlines()
    for row in lines:
        data.append(row.strip())

with open('sales.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['current_date', 'sale_id', 'product_id', 'name', 'price'])
    sale_id = 0
    current_date = datetime.date.today()
    for row in data:
        if row == 'P001':
            sale_id += 1
            csv_writer.writerow([current_date, sale_id, row, 'Wireless Headphones', 100])
        elif row == 'P002':
            sale_id +=1
            csv_writer.writerow([current_date, sale_id, row, 'Laptop Backpack', 60])
        elif row == 'P003':
            sale_id +=1
            csv_writer.writerow([current_date, sale_id, row, 'Bluetooth Speaker', 50])
        elif row == 'P004':
            sale_id +=1
            csv_writer.writerow([current_date, sale_id, row, 'USB Flash Drive', 20])
        elif row == 'P005':
            sale_id +=1
            csv_writer.writerow([current_date, sale_id, row, 'Mobile Phone Case', 15])
        elif row == 'P006':
            sale_id +=1
            csv_writer.writerow([current_date, sale_id, row, 'Wireless Mouse', 30])
        elif row == 'P007':
            sale_id +=1
            csv_writer.writerow([current_date, sale_id, row, 'Laptop Stand', 40])
        elif row == 'P008':
            sale_id +=1
            csv_writer.writerow([current_date, sale_id, row, 'HDMI Cable', 15])
        elif row == 'P009':
            sale_id +=1
            csv_writer.writerow([current_date, sale_id, row, 'Smartphone', 600])
        elif row == 'P010':
            sale_id +=1
            csv_writer.writerow([current_date, sale_id, row, 'External Hard Drive', 100])
        else:
            print(f'unknown product name and price for product id: {row}')