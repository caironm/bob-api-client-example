#!/home/ricardo/.virtualenvs/ferris/bin/python
# -*- coding: utf-8 -*-

import requests
import argparse
import random
from loremipsum import get_sentences

apps = {
    "broker": "https://3-dot-api-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v3",
    "crm": "https://awesome-caster-760.appspot.com/_ah/api/bob/v1",
    "cc": "https://modular-ethos-760.appspot.com/_ah/api/bob/v2",
}

universities = [
    {
        "code": "cc",
        "name": "Slingshot"
    },
    {
        "code": "unitec",
        "name": "Universidad Tecnologica Centroamericana"
    },
    {
        "code": "ceutec",
        "name": "C.E.U.T.E.C."
    },
    {
        "code": "upn",
        "name": "U.P.N."
    },
]

clusters = [
    {
        "code": "AC",
        "name": "Architecture & Construction",
        "name_br": "Arquitetura e Urbanismo",
        "name_es": "Arquitetura y Urbanismo"
    },
    {
        "code": "AG",
        "name": "Agriculture, Food & Natural Resources",
        "name_br": "Agricultura, Alimentação e Recursos Naturais",
        "name_es": ""
    },
    {
        "code": "AR",
        "name": "Arts, A/V Technology & Communications",
        "name_br": "Artes, Tecnologia Audiovisual e Comunicações",
        "name_es": ""
    },
    {
        "code": "BU",
        "name": "Business Management & Administration",
        "name_br": "Gestão e Administração de Negócios",
        "name_es": ""
    },
    {
        "code": "ED",
        "name": "Education & Training",
        "name_br": "Educação e Capacitação",
        "name_es": ""
    },
    {
        "code": "FI",
        "name": "Finance",
        "name_br": "Finanças",
        "name_es": ""
    },
    {
        "code": "GO",
        "name": "Government & Public Administration",
        "name_br": "Administração Governamental e Pública",
        "name_es": ""
    },
    {
        "code": "HS",
        "name": "Health Science",
        "name_br": "Ciências da Saúde",
        "name_es": ""
    },
    {
        "code": "HR",
        "name": "Human Services",
        "name_br": "Serviços Sociais",
        "name_es": ""
    },
    {
        "code": "HT",
        "name": "Hospitality & Tourism",
        "name_br": "Hotelaria e Turismo",
        "name_es": ""
    },
    {
        "code": "IT",
        "name": "Information Technology",
        "name_br": "Tecnologia da Informação",
        "name_es": ""
    },
    {
        "code": "LA",
        "name": "Law, Public Safety, Corrections & Security",
        "name_br": "Direito, Segurança Pública, Serviços Correcionais e Segurança",
        "name_es": ""
    },
    {
        "code": "MF",
        "name": "Manufacturing",
        "name_br": "Manufatura",
        "name_es": ""
    },
    {
        "code": "MK",
        "name": "Marketing",
        "name_br": "Marketing",
        "name_es": ""
    },
    {
        "code": "SC",
        "name": "Science, Technology, Engineering & Math",
        "name_br": "Ciências, Tecnologia, Engenharia e Matemática",
        "name_es": ""
    },
    {
        "code": "TR",
        "name": "Transportation, Distribution & Logistics",
        "name_br": "Transporte, Distribuição e Logística",
        "name_es": ""
    },
]

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
    "-a", "--createaccount",
    type=str,
    help="Create an account with some defaults providing the email")

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

        print("CLUSTERS: %s" % len(response["items"]if "items" in response else []))
    except:
        print("Not a JSON response")
        print("CLUSTERS: Not found")

    # List Universities
    url = "{0}/university/list".format(apps[args.app])

    response = requests.post(url, headers=headers)

    try:
        response = response.json()

        print("UNIVERSITIES: %s" % len(response["items"]if "items" in response else []))
    except:
        print("Not a JSON response")
        print("UNIVERSITIES: Not found")


def insert_cluster(code, name, name_br="", name_es=""):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}

    values = {
        "code": code,
        "name": name,
        "name_br": name_br,
        "name_es": name_es
    }

    url = "{0}/cluster/insert".format(apps[args.app])

    requests.post(url, params=values, headers=headers)


def init_cluster():
    print("Initializing Cluster kind...")

    for cluster in clusters:
        insert_cluster(
            code=cluster["code"],
            name=cluster["name"],
            name_br=cluster["name_br"],
            name_es=cluster["name_es"])

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
        "emailaddress": email,
        "firstname": firstname,
        "paternallastname": paternallastname,
        "maternallastname": maternallastname,
        "password": password,
        "phonenumber": phonenumber,
        "agreement": True,
        "origin": "unitec",
        "portfolioid": ""
    }

    url = "{0}/bob/createaccount".format(apps[args.app])

    print("Creating account for '{0}'...".format(email))

    requests.post(url, params=values, headers=headers)

    try:
        print("done.")
    except:
        print("Not a JSON response")
        print("Failed.")


if __name__ == "__main__":
    if args.clusters:
        init_cluster()

    if args.universities:
        init_university()

    if args.createaccount:
        create_account(args.createaccount)

    default()
