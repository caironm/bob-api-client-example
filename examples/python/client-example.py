#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse
import pyotp

from loremipsum import get_sentences

BOB_CLIENT_VERSION = "1.0"
BOB_CLIENT_NAME = "Bob Client Example"

apps = {
    "dev": "https://3-dot-api-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v3",
}

universities = {
    "upn": "Universiad Privada del Norte",
}

parser = argparse.ArgumentParser()

parser.add_argument(
    "app",
    type=str,
    help="Available apps are ({0})".format(", ".join(apps.keys())),
    choices=apps.keys())

parser.add_argument(
    "university",
    type=str,
    help="Available universities are ({0})".format(
        ", ".join(universities.keys())),
    choices=universities.keys())

parser.add_argument(
    "account",
    type=str,
    help="User's e-mail, the account identifier")

args = parser.parse_args()


def default():
    print "%s v%s" % (BOB_CLIENT_NAME, BOB_CLIENT_VERSION)


def create_account(email, university="upn"):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "BobUniversity": "upn",
        "BobToken": ""}

    t = pyotp.TOTP("R3A7PZLCUQIJFUGX", interval=90)
    token = t.now()

    headers["BobToken"] = str(token)

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
        "Origin": university,
        "PortfolioID": ""
    }

    url = "{0}/bob/createaccount".format(apps[args.app])

    print("Creating account for '{0}' from '{1}'...".format(email, university))

    response = requests.post(url, params=values, headers=headers)

    try:
        print("done.")
        print("Json response:")

        print(response.json())
    except:
        print("Not a JSON response")
        print("Failed.")


if __name__ == "__main__":
    default()

    create_account(
        args.account, args.university if args.university else None)
