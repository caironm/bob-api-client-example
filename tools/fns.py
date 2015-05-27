# -*- coding: utf-8 -*-

import requests
import random
import pyotp
import traceback
import sys
import json

from loremipsum import get_sentences
from settings import apps, universities, countries, clusters, occupations
from settings import completionupdate_results, universities_dict


args = None

MAX_REQUEST_ATTEMPTS = 10


def default():
    print("BOB Client v1.0")


def send_request(url, values, headers=None):
    retries = 0

    response = None

    print('sending request...')

    while retries < MAX_REQUEST_ATTEMPTS:
        try:
            uni_token = universities_dict[args.university]["secret"]

            totp = pyotp.TOTP(uni_token, interval=90)
            token = totp.now()

            if not headers:
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json"}

            headers["BobToken"] = str(token)
            headers["BobKey"] = universities_dict[args.university]["key"]
            headers["BobUniversity"] = args.university or ""
            headers["Content-Length"] = len(json.dumps(values))

            response = requests.post(url, params=values, headers=headers)

            print('attempt #%s' % (retries + 1))
            print(url)

            if response.status_code == 403:
                retries += 1
            else:
                break
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            formatted_exception = traceback.format_exception(
                exc_type, exc_value, exc_traceback)

            print(formatted_exception)

    return response


def list_clusters():
    print("Listing all clusters...")

    values = {}

    url = "{0}/cluster/cluster_list".format(apps[args.app])

    response = send_request(url, values)

    print response
    print(response.content)


def insert_cluster(
        code, name,
        name_es="", name_mx="",
        name_cl="", name_pe="",
        name_ec="", name_br=""):
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

    send_request(url, values)


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


def insert_occupation(
        code, name, description,
        name_es="", name_mx="",
        name_cl="", name_pe="",
        name_ec="", name_br="",
        clusters=""):
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

    send_request(url, values)


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


def insert_university(code, name, country, secret, support_contact):
    values = {
        "code": code,
        "name": name,
        "country": country,
        "secret": secret,
        "support_contact": support_contact
    }

    url = "{0}/university/insert".format(apps[args.app])

    send_request(url, values)


def init_uni():
    print("Initializing University kind...")

    for university in universities:
        insert_university(
            code=university["code"],
            name=university["name"],
            country=university["country"],
            secret=university["secret"],
            support_contact=university["support_contact"])


def cleards():
    print("Clearing datastore...")

    values = {}

    url = "{0}/admin/cleards".format(apps[args.app])

    send_request(url, values)


def insert_country(code, name):
    values = {
        "code": code,
        "name": name
    }

    url = "{0}/country/insert".format(apps[args.app])

    send_request(url, values)


def init_country():
    print("Initializing Country kind...")

    for key in countries.keys():
        insert_country(
            code=key,
            name=countries[key])


def create_account():
    email = "{0}@{1}.net".format(
        get_sentences(1)[0].split(" ")[0],
        get_sentences(1)[0].split(" ")[0]).lower()
    firstname = get_sentences(1)[0].split(" ")[0]
    paternallastname = get_sentences(1)[0].split(" ")[0]
    maternallastname = get_sentences(1)[0].split(" ")[0]
    password = get_sentences(1)[0].split(" ")[0]
    phonenumber = str(random.randint(20000000, 99999999))

    # test data, should return "RECHAZADO"
    if not args.mail:
        firstname = "Mateo"
        paternallastname = "Perez"
        maternallastname = "Perez"
        email = "jonatasm@careercruising.com"

    values = {
        "EmailAddress": args.mail if args.mail else email,
        "FirstName": firstname,
        "PaternalLastName": paternallastname,
        "MaternalLastName": maternallastname,
        "Password": password,
        "PhoneNumber": phonenumber,
        "GradeNumber": random.randint(5, 10),
        "Agreement": True,
        "Origin": args.university,
        "PortfolioID": ""
    }

    url = "{0}/bob/createaccount".format(apps[args.app])

    print("Creating account for '{0}'...".format(
        args.mail if args.mail else email))

    response = send_request(url, values)

    try:
        print(response.content)
    except:
        print("Not a JSON response")
        print("Failed.")


def confirm(portfolioid, message):
    reasons = []

    if message == "RECHAZADO":
        reasons = get_sentences(random.choice([3, 4, 5]))

    values = {
        "Message": message,
        "PortfolioID": portfolioid,
        "Reason": reasons,
        "Origin": args.university
    }

    url = "{0}/bob/confirmation".format(apps[args.app])

    print("Sending {0} confirmation for '{1}'...".format(
        message, portfolioid))

    response = send_request(url, values)

    try:
        print(response.content)
    except:
        print("Not a JSON response")
        print("Failed.")


def completion(portfolioid):
    values = completionupdate_results[random.choice([0, 1])]

    headers = None

    values["PortfolioID"] = portfolioid
    values["ResultURL"] += portfolioid
    values["MMDate"] = "22/11/2014"
    values["TerminosCC"] = "1"

    url = "{0}/bob/completionupdate".format(apps[args.app])

    print("Sending completion update notification for '{0}'...".format(
        portfolioid))

    response = None

    response = send_request(url, values, headers=headers)

    try:
        print(response.content)
    except:
        print("Not a JSON response")
        print("Failed.")


def phoneupdate(portfolioid):
    values = {}

    headers = None

    values["PortfolioID"] = portfolioid
    values["PhoneNumber"] = str(int(random.random() * 1000000))
    values["MMDate"] = "22/11/2014"
    values["TerminosCC"] = "1"
    values["Cluster1"] = ""
    values["Cluster2"] = ""

    url = "{0}/bob/completionupdate".format(apps[args.app])

    print("Sending phone update notification for '{0}'...".format(
        portfolioid))

    response = None

    response = send_request(url, values, headers=headers)

    try:
        print(response.content)
    except:
        print("Not a JSON response")
        print("Failed.")
