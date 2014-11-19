#!/home/ricardo/.virtualenvs/ferris/bin/python
# -*- coding: utf-8 -*-

import requests
import argparse

from loremipsum import get_sentences
from settings import apps, universities, countries, clusters, occupations, init

parser = argparse.ArgumentParser()

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
    type=str,
    help="Account email, create an account with some defaults")

parser.add_argument(
    "-d", "--directory",
    type=str,
    help="Directory where all configuration data live")

parser.add_argument(
    "-sq", "--stock",
    type=str,
    help="Query stock quote from a particular company")

args = parser.parse_args()


def default():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    # List Countries
    url = "{0}/country/list".format(apps[args.app])

    response = requests.post(url, headers=headers)

    try:
        response = response.json()

        print("COUNTRIES: %s" % len(
            response["items"]if "items" in response else []))
    except:
        print("Not a JSON response")
        print("COUNTRIES: Not found")

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

    # List Occupations
    url = "{0}/occupation/list".format(apps[args.app])

    response = requests.post(url, headers=headers)

    try:
        response = response.json()

        print("OCCUPATIONS: %s" % len(
            response["items"]if "items" in response else []))
    except:
        print("Not a JSON response")
        print("OCCUPATIONS: Not found")


def insert_cluster(
        code, name,
        name_es="", name_mx="",
        name_cl="", name_pe="",
        name_ec="", name_br=""):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    uni_list_selected = []

    if len(name_mx.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "mx"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    if len(name_cl.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "cl"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    if len(name_pe.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "pe"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    if len(name_ec.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "ec"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    if len(name_br.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "br"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    values = {
        "code": code,
        "name": name,
        "name_es": name_es,
        "name_mx": name_mx,
        "name_cl": name_cl,
        "name_pe": name_pe,
        "name_ec": name_ec,
        "name_br": name_br,
        "universities": ",".join(uni_list_selected)
    }

    url = "{0}/cluster/insert".format(apps[args.app])

    requests.post(url, params=values, headers=headers)


def init_cluster():
    print("Initializing Cluster kind...")

    for key in clusters:
        cluster = clusters[key]
        insert_cluster(
            code=cluster["code"],
            name=cluster["name"],
            name_es=cluster["name_es"],
            name_mx=cluster["name_mx"],
            name_cl=cluster["name_cl"],
            name_pe=cluster["name_pe"],
            name_ec=cluster["name_ec"],
            name_br=cluster["name_br"]
        )

    print("done.")


def insert_occupation(
        code, name, description,
        name_es="", name_mx="",
        name_cl="", name_pe="",
        name_ec="", name_br="",
        clusters=""):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    uni_list_selected = []

    if len(name_mx.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "mx"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    if len(name_cl.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "cl"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    if len(name_pe.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "pe"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    if len(name_ec.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "ec"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    if len(name_br.strip()) > 0:
        uni_list = [u["code"] for u in universities if u["country"] == "br"]
        for uni in uni_list:
            uni_list_selected.append(uni)

    values = {
        "code": code,
        "name": name,
        "description": description,
        "name_es": name_es,
        "name_mx": name_mx,
        "name_cl": name_cl,
        "name_pe": name_pe,
        "name_ec": name_ec,
        "name_br": name_br,
        "universities": ",".join(uni_list_selected),
        "clusters": clusters
    }

    url = "{0}/occupation/insert".format(apps[args.app])

    requests.post(url, params=values, headers=headers)


def init_occupation():
    print("Initializing Occupation kind...")

    for key in occupations:
        occupation = occupations[key]

        name_es = occupation["name_es"] if "name_es" in occupation else ""
        name_mx = occupation["name_mx"] if "name_mx" in occupation else ""
        name_cl = occupation["name_cl"] if "name_cl" in occupation else ""
        name_pe = occupation["name_pe"] if "name_pe" in occupation else ""
        name_ec = occupation["name_ec"] if "name_ec" in occupation else ""
        name_br = occupation["name_br"] if "name_br" in occupation else ""

        insert_occupation(
            code=occupation["code"],
            name=occupation["name"],
            description=occupation["description"],
            name_es=name_es,
            name_mx=name_mx,
            name_cl=name_cl,
            name_pe=name_pe,
            name_ec=name_ec,
            name_br=name_br,
            clusters=occupation["clusters"]
        )

    print("done.")


def insert_university(code, name, country):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    values = {
        "code": code,
        "name": name,
        "country": country
    }

    url = "{0}/university/insert".format(apps[args.app])

    requests.post(url, params=values, headers=headers)


def init_uni():
    print("Initializing University kind...")

    for university in universities:
        insert_university(
            code=university["code"],
            name=university["name"], country=university["country"])

    print("done.")


def insert_country(code, name):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    values = {
        "code": code,
        "name": name
    }

    url = "{0}/country/insert".format(apps[args.app])

    requests.post(url, params=values, headers=headers)


def init_country():
    print("Initializing Country kind...")

    for key in countries.keys():
        insert_country(
            code=key,
            name=countries[key])

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
    if args.account:
        if args.university:
            create_account(args.account)
        else:
            print(
                "Specify a univeristy: -v {%s}" % ",".join(
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

    if args.stock:
        print stock_quote(args.stock)

    default()
