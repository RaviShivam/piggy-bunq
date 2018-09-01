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
        dummy_policy_obj = [
            {
                "shop": "Starbucks",
                "discount_policy": [
                    (0, 100, 0.05),
                    (101, 200, 0.1),
                    (201, 300, 0.15)
                ],
                "loot_discounts": {
                    "type": "FIRST_PAYMENT_DISCOUNT",
                    "value": 0.5
                },
                "current_points": 10
            }
        ]

        with open(self.discount_policy_file, 'w') as outfile:
            json.dump(dummy_policy_obj, outfile)


if __name__=="__main__":
    user_discounts = UserDiscounts()
    discounts = user_discounts.get_discounts()
    print(discounts)