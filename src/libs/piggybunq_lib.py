import csv
import json
from datetime import datetime

from libs.bunq_lib import BunqLib
from libs.share_lib import ShareLib


def parse_user_discounts(file):
    "Returns list of dictionaries with all the discounts in them"
    readCSV = csv.reader(open(file))
    c = 0
    discounts = []
    for r in readCSV:
        if c == 0:
            c += 1
            headers = r
            continue
        discounts.append(dict(zip(headers, r)))
    return discounts


def determine_discount(description, user):
    """
    Determine whether a particular (not yet conducted) payment is eligible for a discount
    - Description has to match the shop name
    - current date should be later than the start date
    - counts left should be more than 0
    """
    currentdate = datetime.now()
    for d in user['discounts']:
        if description == d['shop']:
            print(d)
            if d['loot_discounts']:
                dsc_item = d['loot_discounts'].pop(0)
                is_valid = currentdate > datetime.strptime(dsc_item['valid_from'], "%d-%m-%Y")
                if is_valid:
                    # if dsc_item['type'] == "FIRST_PAYMENT_DISCOUNT":
                    return d['shop'], dsc_item['value']
            else:
                for r in d['discount_policy']:
                    if r[0] <= d["current_points"] <= r[1]:
                        return d['shop'], r[2]
    return None, 0


def make_payment_w_discount(amount, description, recipient, discounts):
    """
    Wrapper around bunq `make_payment` function.
    Calculates the discount specific to a user.
    """
    all_option = ShareLib.parse_all_option()
    environment_type = ShareLib.determine_environment_type_from_all_option(all_option)

    ShareLib.print_header()

    bunq = BunqLib(environment_type)

    shop, user_discount = determine_discount(description, discounts) * amount

    # Request data from sugar daddy (advance payment)
    bunq.make_request(user_discount, "-".join("ADVANCE", shop, user_discount), "sugardaddy@bunq.com")

    # Make actual payment to the shop
    bunq.make_payment(amount - user_discount, description, recipient)

    # Send data to front-end


def userhistory_to_json(userperson, payment_history, discounts):
    """
    Deprecated with the use of Database
    """
    json_payments = {"class": "payment_history", "name": userperson.legal_name, "payments": []}
    json_discounts = {"class": "discounts", "name": userperson.legal_name, "discounts": []}
    for p in payment_history:
        json_payments['payments'].append(payment_to_json(userperson, p, discounts))

    for d in discounts:
        json_discounts['discounts'].append({
            "shop": d[0],
            "discount": d[1],
            "validFrom": d[2],
            "validTo": d[3],
            "maxCount": d[4]
        })
    return json.dumps(json_payments), json.dumps(json_discounts)


def payment_to_json(userperson, payment, discounts=None):
    personal_discount = 0
    json_payment = {
        "class": "new_payment",
        "name": userperson.legal_name,
        "shop": payment.description,
        "value": payment.amount.value,
        "currency": payment.amount.currency,
        "discount": personal_discount
    }
    return json_payment
