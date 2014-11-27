#!/home/ricardo/.virtualenvs/ferris/bin/python
# -*- coding: utf-8 -*-

import argparse
import fns

from settings import apps, universities, init

from fns import default, init_cluster
from fns import init_occupation, init_uni
from fns import init_country, create_account, confirm, completion

parser = argparse.ArgumentParser()

parser.add_argument(
    "-v", "--verbose",
    help="Show details about the data in the datastore",
    action="store_true")

parser.add_argument(
    "-init", "--initialize",
    help="Initialize the data store",
    action="store_true")

parser.add_argument(
    "app",
    type=str,
    help="Available apps are ({0})".format(", ".join(apps.keys())),
    choices=apps.keys())

parser.add_argument(
    "-u", "--university",
    type=str,
    help="Available universities are ({0})".format(
        ", ".join([u["code"] for u in universities])),
    choices=[u["code"] for u in universities])

parser.add_argument(
    "-a", "--account",
    help="Account email, create an account with some defaults",
    action="store_true")

parser.add_argument(
    "-cu", "--completionupdate",
    type=str,
    help="Portfolio ID to be updated after tests have ended")

parser.add_argument(
    "-c", "--confirm",
    type=str,
    help="Portfolio ID to be confirmed")

parser.add_argument(
    "-r", "--reject",
    type=str,
    help="Portfolio ID to be rejected")

parser.add_argument(
    "-d", "--directory",
    type=str,
    help="Directory where all configuration data live")

parser.add_argument(
    "-m", "--mail",
    type=str,
    help="Specify the email to use when creating an account")


if __name__ == "__main__":
    args = parser.parse_args()
    fns.args = args

    if args.account:
        if args.university:
            create_account()
        else:
            print(
                "Specify a univeristy: -u {%s}" % ",".join(
                    [u["code"] for u in universities]))

    if args.confirm:
        if args.university:
            confirm(args.confirm, "ACEPTADO")
        else:
            print(
                "Specify a univeristy: -u {%s}" % ",".join(
                    [u["code"] for u in universities]))

    if args.completionupdate:
        completion(args.completionupdate)

    if args.reject:
        if args.university:
            confirm(args.reject, "RECHAZADO")
        else:
            print(
                "Specify a univeristy: -u {%s}" % ",".join(
                    [u["code"] for u in universities]))

    if args.initialize:
        if args.directory:
            init(args.directory)
            init_country()
            init_uni()
            init_cluster()
            init_occupation()
        else:
            print("Specify the data directory: -d DIRECTORY")

    if args.verbose:
        default()
