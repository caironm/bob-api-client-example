#!/home/ricardo/.virtualenvs/ferris/bin/python
# -*- coding: utf-8 -*-

import requests
import argparse
from loremipsum import get_sentences

apps = {
    "broker": "https://3-dot-api-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v3",
    "local": "http://localhost:8080/_ah/api/bob/v3"
}

universities = [
    {
        "code": "bob",
        "name": "Bob Service"
    },
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
        "name_es": "Arquitectura"
    },
    {
        "code": "AG",
        "name": "Agriculture, Food & Natural Resources",
        "name_br": "Agricultura, Alimentação e Recursos Naturais",
        "name_es": "Administración y Agronegocios"
    },
    {
        "code": "AR",
        "name": "Arts, A/V Technology & Communications",
        "name_br": "Artes, Tecnologia Audiovisual e Comunicações",
        "name_es": "Artes contemporáneas"
    },
    {
        "code": "BU",
        "name": "Business Management & Administration",
        "name_br": "Gestão e Administração de Negócios",
        "name_es": "Administración y Negocios"
    },
    {
        "code": "ED",
        "name": "Education & Training",
        "name_br": "Educação e Capacitação",
        "name_es": "Educación"
    },
    {
        "code": "FI",
        "name": "Finance",
        "name_br": "Finanças",
        "name_es": "Economía y Finanzas"
    },
    {
        "code": "GO",
        "name": "Government & Public Administration",
        "name_br": "Administração Governamental e Pública",
        "name_es": "Gobierno y Administración Pública"
    },
    {
        "code": "HE",
        "name": "Health Science",
        "name_br": "Ciências da Saúde",
        "name_es": "Ciencias de la Salud"
    },
    {
        "code": "HS",
        "name": "Human Services",
        "name_br": "Serviços Sociais",
        "name_es": "Ciencias Humanas"
    },
    {
        "code": "HT",
        "name": "Hospitality & Tourism",
        "name_br": "Hotelaria e Turismo",
        "name_es": "Hotelería"
    },
    {
        "code": "IT",
        "name": "Information Technology",
        "name_br": "Tecnologia da Informação",
        "name_es": "Tecnología informática"
    },
    {
        "code": "LA",
        "name": "Law, Public Safety, Corrections & Security",
        "name_br": "Direito, Segurança Pública, Serviços Correcionais e Segurança",
        "name_es": "Derecho"
    },
    {
        "code": "MF",
        "name": "Manufacturing",
        "name_br": "Manufatura",
        "name_es": "Ingeniería Industrial"
    },
    {
        "code": "MK",
        "name": "Marketing",
        "name_br": "Marketing",
        "name_es": "Marketing"
    },
    {
        "code": "SC",
        "name": "Science, Technology, Engineering & Math",
        "name_br": "Ciências, Tecnologia, Engenharia e Matemática",
        "name_es": "Ciencias, Ingeniería y Tecnología"
    },
    {
        "code": "TR",
        "name": "Transportation, Distribution & Logistics",
        "name_br": "Transporte, Distribuição e Logística",
        "name_es": "Distribución y logística"
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
        "EmailAddress": email,
        "FirstName": firstname,
        "PaternalLastName": paternallastname,
        "MaternalLastName": maternallastname,
        "Password": password,
        "PhoneNumber": phonenumber,
        "Agreement": True,
        "Origin": "upn",
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
