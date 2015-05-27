#!/home/ricardo/.virtualenvs/ferris/bin/python
# -*- coding: utf-8 -*-

import argparse
import fns

from settings import apps, universities, init

from fns import default, init_cluster, cleards
from fns import init_occupation, init_uni, list_clusters
from fns import init_country, create_account, confirm, completion
from fns import phoneupdate

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
    "-pu", "--phoneupdate",
    type=str,
    help="Portfolio ID to be updated after tests have ended")

parser.add_argument(
    "-cds", "--cleardatastore",
    help="Clear the datastore before any further operations",
    action="store_true")

parser.add_argument(
    "-c", "--confirm",
    type=str,
    help="Portfolio ID to be confirmed")

parser.add_argument(
    "-cs", "--clusters",
    help="List all clusters",
    action="store_true")

parser.add_argument(
    "-r", "--reject",
    type=str,
    help="Portfolio ID to be rejected")

parser.add_argument(
    "-d", "--directory",
    type=str,
    help="Directory where all configuration data live")

parser.add_argument(
    "-t", "--token",
    type=str,
    help="Bob token secret")

parser.add_argument(
    "-m", "--mail",
    type=str,
    help="Specify the email to use when creating an account")


if __name__ == "__main__":
    args = parser.parse_args()
    fns.args = args

    if fns.args.cleardatastore:
        cleards()

    if fns.args.clusters:
        list_clusters()

    if fns.args.account:
        if fns.args.university:
            create_account()
        else:
            print(
                "Specify a univeristy: -u {%s}" % ",".join(
                    [u["code"] for u in universities]))

    if fns.args.confirm:
        if fns.args.university:
            confirm(fns.args.confirm, "ACEPTADO")
        else:
            print(
                "Specify a univeristy: -u {%s}" % ",".join(
                    [u["code"] for u in universities]))

    if fns.args.completionupdate:
        completion(fns.args.completionupdate)

    if fns.args.phoneupdate:
        phoneupdate(fns.args.phoneupdate)

    if fns.args.reject:
        if fns.args.university:
            confirm(fns.args.reject, "RECHAZADO")
        else:
            print(
                "Specify a univeristy: -u {%s}" % ",".join(
                    [u["code"] for u in universities]))

    if fns.args.initialize:
        if fns.args.directory:
            init(args.directory)
            init_country()
            init_uni()
            init_cluster()
            init_occupation()
        else:
            print("Specify the data directory: -d DIRECTORY")

    if args.verbose:
        default()
