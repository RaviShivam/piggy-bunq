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
                    "category": "Coffee",
                    "discount_policy": [
                        (0, 100, 0.05),
                        (101, 200, 0.1),
                        (201, 300, 0.15)
                    ],
                    "loot_discounts": [{
                        "type": "FREQUENT BUCKER",
                        "value": 0.2,
                        "valid_from": "02-08-2018",
                        "valid_to": "18-09-2018",
                    }],
                    "current_points": 100
                }, {
                    "shop": "Kwekkeboom",
                    "category": "Coffee",
                    "discount_policy": [
                        (0, 20, 0.05),
                        (21, 100, 0.1),
                        (100, 200, 0.15),
                    ],
                    "loot_discounts": [],
                    "current_points": 40
                }, {
                    "shop": "Game Mania",
                    "category": "Gaming",
                    "discount_policy": [
                        (0, 100, 0.05),
                        (101, 400, 0.15),
                        (400, 800, 0.25)
                    ],
                    "loot_discounts": [{
                        "type": "FIRST PAYMENT DISCOUNT",
                        "value": 0.25,
                        "valid_from": "10-09-2018",
                        "valid_to": "25-09-2018",
                    }],
                    "current_points": 0
                }, {
                    "shop": "Oude Jan",
                    "category": "Bar",
                    "discount_policy": [
                        (0, 100, 0.05),
                        (101, 400, 0.15),
                        (400, 800, 0.25)
                    ],
                    "loot_discounts": [{
                        "type": "SPECIAL GOLDEN BIRD",
                        "value": 0.5,
                        "valid_from": "15-09-2018",
                        "valid_to": "30-09-2018",
                    }],
                    "current_points": 100
                }, {
                    "shop": "Slijterij Sital",
                    "category": "Alcohol",
                    "discount_policy": [
                        (0, 200, 0.05),
                        (101, 400, 0.15),
                        (400, 800, 0.25)
                    ],
                    "loot_discounts": [{
                        "type": "GOLD RARE",
                        "value": 0.4,
                        "valid_from": "15-08-2018",
                        "valid_to": "30-10-2018",
                    }],
                    "current_points": 30
                }, {
                    "shop": "Spar",
                    "category": "Grocery",
                    "discount_policy": [
                        (0, 200, 0.05),
                        (101, 400, 0.10),
                        (400, 800, 0.20)
                    ],
                    "loot_discounts": [{
                        "type": "BUNQ LOOT",
                        "value": 0.3,
                        "valid_from": "10-09-2018",
                        "valid_to": "25-10-2018",
                    }],
                    "current_points": 50
                }, {
                    "shop": "Jumbo",
                    "category": "Grocery",
                    "discount_policy": [
                        (0, 200, 0.05),
                        (101, 400, 0.10),
                        (400, 800, 0.20)
                    ],
                    "loot_discounts": [],
                    "current_points": 75
                }

            ]
        }
        with open(self.discount_policy_file, 'w') as outfile:
            json.dump(dummy_policy_obj, outfile)


if __name__ == "__main__":
    user_discounts = UserDiscounts()
    discounts = user_discounts.get_discounts()
    print(discounts)
