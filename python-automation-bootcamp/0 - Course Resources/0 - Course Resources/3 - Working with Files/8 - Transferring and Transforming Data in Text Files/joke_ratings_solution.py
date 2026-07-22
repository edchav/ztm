import csv


def rating_category(rating):
    rating = int(rating)

    if rating <= -3:
        category = 'abysmal'
    elif rating <= -1:
        category = 'awful'
    else:
        category = 'bad'

    return category


modified_dad_jokes = []

with open('dad_jokes.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    headers = next(csv_reader)
    headers.append('rating_category')

    modified_dad_jokes.append(headers)

    for row in csv_reader:
        row.append(rating_category(row[2]))

        modified_dad_jokes.append(row)


with open('modified_dad_jokes.csv','w',newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)

    csv_writer.writerows(modified_dad_jokes)


