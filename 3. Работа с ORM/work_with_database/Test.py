import csv
from pprint import pprint

with open('phones.csv', 'r') as file:
    phones = list(csv.DictReader(file, delimiter=';'))

if __name__ == "__main__":
    for phone in phones:
        model = Phone(
            name=phone["name"],
            price=phone["price"],
            image=phone["image"],
            release_date=phone["release_date"],
            lte_exists=phone["lte_exists"],
            slug=phone["slug"],
        )