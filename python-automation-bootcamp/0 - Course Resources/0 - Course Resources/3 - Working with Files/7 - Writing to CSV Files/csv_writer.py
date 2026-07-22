# ['Max','Dog', 'bacon strips',4754]
# ['Julius','Cat','catnip',3215]
# ['Cal','Cat','anything edible',71142]
# ['Lena','Cat','Sheba',142]
# ['Bruiser','Featherfin Catfish','fish pellets',54]

import csv

with open('expensive_pets.csv','w',newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(['name','species','favorite_snack','monthly_cost'])
    csv_writer.writerow(['Max','Dog', 'bacon strips',4754])

    csv_writer.writerows([['Julius','Cat','catnip',3215],
                          ['Cal','Cat','anything edible',71142],
                          ['Lena','Cat','Sheba',142],
                          ['Bruiser','Featherfin Catfish','fish pellets',54]])
