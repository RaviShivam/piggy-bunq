#!/usr/bin/env .venv/bin/python -W ignore
from libs.bunq_lib import BunqLib
from libs.share_lib import ShareLib
import csv
import random
import time

def import_shops_csv():
    shops = []
    with open('data/shops.csv', 'r') as csvfile:
        line = csv.reader(csvfile, delimiter=',')
        line_count = 0
        for row in line:
            if line_count != 0:
                shops.append(row)
            line_count += 1

    return shops


def generate_random_entry():
    shops = import_shops_csv()
    random_shop_name, random_shop_category = random.choice(shops)
    price = random.randint(10, 100)
    return price, 'Game Mania', "4.89 53.2 12 100 NL"



def main():
    all_option = ShareLib.parse_all_option()
    environment_type = ShareLib.determine_environment_type_from_all_option(all_option)

    ShareLib.print_header()

    bunq = BunqLib(environment_type)


    for i in range(1):
        amount, description, geolocation = generate_random_entry()
        print(amount, description, geolocation)
        recipient = "griffin.courtland@bunq.nl"

        bunq.make_payment(str(amount), description, recipient, geolocation=geolocation)
        time.sleep(1)

if __name__ == "__main__":
    main()