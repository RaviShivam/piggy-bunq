#!/usr/bin/env .venv/bin/python -W ignore
from libs.bunq_lib import BunqLib
from libs.share_lib import ShareLib
from db_helper import DbHelper
from threading import Thread
import time

from src.libs.piggybunq_lib import parse_user_discounts, determine_discount


def refresh_database(bunq, discounts):
    database = DbHelper()
    existing_tx = [tranx[0] for tranx in database.get_payments_from_database()]
    while True:
        new_payments = bunq.get_all_payment(5)
        for np in new_payments:
            if np.id_ not in existing_tx and np.description.split("-")[0] != "CASHBACK":
                _, dsc = determine_discount(np.description, discounts)
                database.add_payment_to_database(np.id_, np.description, np.amount.value,
                                                 np._alias.label_monetary_account.display_name, dsc)
                pass
        time.sleep(3)


def main():
    all_option = ShareLib.parse_all_option()
    environment_type = ShareLib.determine_environment_type_from_all_option(all_option)

    ShareLib.print_header()

    bunq = BunqLib(environment_type)

    user = bunq.get_current_user()

    discounts = parse_user_discounts("data/discount.csv")

    database = DbHelper()

    Thread(target=refresh_database, args=(bunq, discounts)).start()

    # all_request = bunq.get_all_request(1)
    # ShareLib.print_all_request(all_request)
    #
    # all_card = bunq.get_all_card(1)
    # ShareLib.print_all_card(all_card, all_monetary_account_bank_active)
    #
    # if environment_type is ApiEnvironmentType.SANDBOX:
    #     all_alias = bunq.get_all_user_alias()
    #     ShareLib.print_all_user_alias(all_alias)
    #
    # bunq.update_context()


if __name__ == '__main__':
    main()
