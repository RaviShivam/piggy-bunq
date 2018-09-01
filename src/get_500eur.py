#!/usr/bin/env .venv/bin/python -W ignore
from libs.bunq_lib import BunqLib
from libs.share_lib import ShareLib


def main():
    all_option = ShareLib.parse_all_option()
    environment_type = ShareLib.determine_environment_type_from_all_option(all_option)

    ShareLib.print_header()

    bunq = BunqLib(environment_type)

    bunq.make_request("500", "none", "sugardaddy@bunq.com")

    all_request = bunq.get_all_request(10)
    ShareLib.print_all_request(all_request)

    bunq.update_context()


if __name__ == '__main__':
    main()
