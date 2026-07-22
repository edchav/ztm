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


