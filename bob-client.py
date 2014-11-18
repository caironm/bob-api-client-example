#!/home/ricardo/.virtualenvs/ferris/bin/python
# -*- coding: utf-8 -*-

import requests
import argparse

from loremipsum import get_sentences
from settings import apps, universities, clusters

parser = argparse.ArgumentParser()

parser.add_argument(
    "-c", "--clusters",
    help="Initialize the Cluster kind with some data",
    action="store_true")

parser.add_argument(
    "-u", "--universities",
    help="Initialize the University kind with some data",
    action="store_true")

parser.add_argument(
    "app",
    type=str,
    help="Available apps are ({0})".format(", ".join(apps.keys())),
    choices=apps.keys())

parser.add_argument(
    "university",
    type=str,
    help="Available universities are ({0})".format(
        ", ".join([u["code"] for u in universities])),
    choices=[u["code"] for u in universities])

parser.add_argument(
    "-a", "--account",
    type=str,
    help="Create an account with some defaults providing the email")

parser.add_argument(
    "-sq", "--stock",
    type=str,
    help="Query stock quote from a particular company")

args = parser.parse_args()


def default():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    # List Clusters
    url = "{0}/cluster/list".format(apps[args.app])

    response = requests.post(url, headers=headers)

    try:
        response = response.json()

        print("CLUSTERS: %s" % len(
            response["items"]if "items" in response else []))
    except:
        print("Not a JSON response")
        print("CLUSTERS: Not found")

    # List Universities
    url = "{0}/university/list".format(apps[args.app])

    response = requests.post(url, headers=headers)

    try:
        response = response.json()

        print("UNIVERSITIES: %s" % len(
            response["items"]if "items" in response else []))
    except:
        print("Not a JSON response")
        print("UNIVERSITIES: Not found")


def insert_cluster(code, name, name_local=""):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    values = {
        "university": args.university,
        "code": code,
        "name": name,
        "name_local": name_local
    }

    url = "{0}/cluster/insert".format(apps[args.app])

    requests.post(url, params=values, headers=headers)


def init_cluster():
    print("Initializing Cluster kind...")

    for cluster in clusters[args.university]:
        insert_cluster(
            code=cluster["code"],
            name=cluster["name"],
            name_local=cluster["name_local"])

    print("done.")


def insert_university(code, name):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    values = {
        "code": code,
        "name": name
    }

    url = "{0}/university/insert".format(apps[args.app])

    requests.post(url, params=values, headers=headers)


def init_university():
    print("Initializing University kind...")

    for university in universities:
        insert_university(code=university["code"], name=university["name"])

    print("done.")


def create_account(email):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    firstname = get_sentences(1)[0].split(" ")[0]
    paternallastname = get_sentences(1)[0].split(" ")[0]
    maternallastname = get_sentences(1)[0].split(" ")[0]
    password = get_sentences(1)[0].split(" ")[0]
    phonenumber = get_sentences(1)[0].split(" ")[0].upper()

    values = {
        "EmailAddress": email,
        "FirstName": firstname,
        "PaternalLastName": paternallastname,
        "MaternalLastName": maternallastname,
        "Password": password,
        "PhoneNumber": phonenumber,
        "Agreement": True,
        "Origin": args.university,
        "PortfolioID": ""
    }

    url = "{0}/bob/createaccount".format(apps[args.app])

    print("Creating account for '{0}'...".format(email))

    response = requests.post(url, params=values, headers=headers)

    try:
        print("done.")
        print(response)
    except:
        print("Not a JSON response")
        print("Failed.")


def stock_quote(symbol):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    values = {
        "symbol": symbol.upper()
    }

    url = "{0}/bob/stockquote".format(apps[args.app])

    print("Getting stock quote of {0}...".format(symbol.upper()))

    response = requests.post(url, params=values, headers=headers)

    print("done")

    try:
        quote = response.json()

        return "{0}: {1} {2}".format(
            symbol.upper(), quote["price_last"], quote["price_change"])
    except:
        return response


if __name__ == "__main__":
    if args.clusters:
        init_cluster()

    if args.universities:
        init_university()

    if args.account:
        create_account(args.account)

    if args.stock:
        print stock_quote(args.stock)

    default()
