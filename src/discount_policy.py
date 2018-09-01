import os
import json


class UserDiscounts:
    discount_policy_file = 'db/discounts.json'

    def __init__(self):
        if not os.path.isfile(self.discount_policy_file):
            self.initialize_policy_file()

    def get_discounts(self):
        with open(self.discount_policy_file, 'r') as file:
            return json.load(file)

    def initialize_policy_file(self):
        dummy_policy_obj = {
            "user": "Jan",
            "discounts": [
                {
                    "shop": "Starbucks",
                    "discount_policy": [
                        (0, 100, 0.05),
                        (101, 200, 0.1),
                        (201, 300, 0.15)
                    ],
                    "loot_discounts": [{
                        "type": "FIRST_PAYMENT_DISCOUNT",
                        "value": 0.5,
                        "valid_from": "02-08-2018",
                        "valid_to": "18-08-2018",
                    }],
                    "current_points": 0
                }, {
                    "shop": "Kwekkeboom",
                    "discount_policy": [
                        (0, 20, 0.05),
                        (21, 100, 0.1),
                        (100, 200, 0.15),
                    ],
                    "loot_discounts": [],
                    "current_points": 25
                }, {
                    "shop": "Game Mania",
                    "discount_policy": [
                        (0, 100, 0.05),
                        (101, 400, 0.15),
                        (400, 800, 0.25)
                    ],
                    "loot_discounts": [{
                        "type": "FIRST_PAYMENT_DISCOUNT",
                        "value": 0.25,
                        "valid_from": "10-08-2018",
                        "valid_to": "25-08-2018",
                    }],
                    "current_points": 95
                }, {
                    "shop": "Oude",
                    "discount_policy": [
                        (0, 100, 0.05),
                        (101, 400, 0.15),
                        (400, 800, 0.25)
                    ],
                    "loot_discounts": [{
                        "type": "DOUBLE_YOUR_POINTS",
                        "value": 0,
                        "valid_from": "15-08-2018",
                        "valid_to": "30-08-2018",
                    }],
                    "current_points": 95
                }

            ]
        }
        with open(self.discount_policy_file, 'w') as outfile:
            json.dump(dummy_policy_obj, outfile)


if __name__ == "__main__":
    user_discounts = UserDiscounts()
    discounts = user_discounts.get_discounts()
    print(discounts)
