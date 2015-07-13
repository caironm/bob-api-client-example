# -*- coding: utf-8 -*-

import os
import csv

apps = {
    "local": "http://localhost:8080/_ah/api/bob/v1",
    "localui": "http://localhost:8080/_ah/api/ui/v1",
    "qa": "https://1-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v1",
    "qaui": "https://1-dot-dazzling-rex-760.appspot.com/_ah/api/ui/v1",
    "qa2": "https://2-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v1",
}

countries = {
    "hn": "Honduras",
    "mx": "Mexico",
    "cl": "Chile",
    "pe": "Peru",
    "ec": "Ecuador",
    "br": "Brazil",
    "us": "United States of America",
}

universities = [
    {
        "code": "bob",
        "name": "Bob Service",
        "country": "hn",
        "secret": "DPM5ATFPXV43SH65",
        "key": "",
        "key": "325ffeda-d43c-4a35-994a-75a5e1e9bfe6",
        "support_contact": "ricr.sb@gmail.com"
    },
    {
        "code": "lnpsbi",
        "name": "LNPS BI",
        "country": "hn",
        "secret": "5PJAK6PJXYEB2ACL",
        "key": "05712b18-b457-4722-8732-7c32d980eb13",
        "support_contact": "ricr.sb@gmail.com"
    },
    {
        "code": "cc",
        "name": "Slingshot",
        "country": "us",
        "secret": "VY72IUVROA6LTYHK",
        "key": "325ffeda-d43c-4a35-994a-75a5e1e9bfe6",
        "support_contact": "ricr.sb@gmail.com"
    },
    {
        "code": "upn",
        "name": "Universidad Privada del Norte",
        "country": "pe",
        "secret": "R3A7PZLCUQIJFUGX",
        "key": "84b839d4-bee0-428a-880c-83fac0f98485",
        "support_contact": "ricr.sb@gmail.com"
    },
    {
        "code": "uvmchile",
        "name": "Universidad Vina del Mar",
        "country": "br",
        "secret": "37DOKPKC46QHEP45",
        "key": "325ffeda-d43c-4a35-994a-75a5e1e9bfe6",
        "support_contact": "ricr.sb@gmail.com"
    },
]

universities_dict = {
    "bob": {
        "code": "bob",
        "name": "Bob Service",
        "country": "hn",
        "secret": "DPM5ATFPXV43SH65",
        "key": "325ffeda-d43c-4a35-994a-75a5e1e9bfe6",
        "support_contact": "ricr.sb@gmail.com"
    },
    "lnpsbi": {
        "code": "lnpsbi",
        "name": "LNPS BI",
        "country": "hn",
        "secret": "5PJAK6PJXYEB2ACL",
        "key": "05712b18-b457-4722-8732-7c32d980eb13",
        "support_contact": "ricr.sb@gmail.com"
    },
    "cc": {
        "code": "cc",
        "name": "Slingshot",
        "country": "us",
        "secret": "VY72IUVROA6LTYHK",
        "key": "325ffeda-d43c-4a35-994a-75a5e1e9bfe6",
        "support_contact": "ricr.sb@gmail.com"
    },
    "upn": {
        "code": "upn",
        "name": "Universidad Privada del Norte",
        "country": "pe",
        "secret": "R3A7PZLCUQIJFUGX",
        "key": "84b839d4-bee0-428a-880c-83fac0f98485",
        "support_contact": "ricr.sb@gmail.com"
    },
    "uvmchile": {
        "code": "uvm-cl",
        "name": "Universidad Vina del Mar",
        "country": "br",
        "secret": "37DOKPKC46QHEP45",
        "key": "325ffeda-d43c-4a35-994a-75a5e1e9bfe6",
        "support_contact": "ricr.sb@gmail.com"
    },
}

clusters = {}

occupations = {}

completionupdate_results = [
    {
        "PortfolioID": "",
        "MMDate": "06/16/2014",
        "Cluster1": "Ciencias Humanas",
        "Cluster2": "Ciencias de la Salud",
        "ResultURL": "https://www2.careercruising.com/Default/Laureate?PortfolioId=",
        "PhoneNumber": "22334455",
        "Ocupaciones1Cluster1": "",
        "Ocupaciones2Cluster1": "",
        "Ocupaciones3Cluster1": "",
        "Ocupaciones4Cluster1": "",
        "Ocupaciones5Cluster1": "",
        "Ocupaciones6Cluster1": "",
        "Ocupaciones7Cluster1": "",
        "Ocupaciones8Cluster1": "",
        "Ocupaciones9Cluster1": "",
        "Ocupaciones10Cluster1": "",
        "Aptitudes1Cluster1": "",
        "Aptitudes2Cluster1": "",
        "Aptitudes3Cluster1": "",
        "Aptitudes4Cluster1": "",
        "Aptitudes5Cluster1": "",
        "Aptitudes6Cluster1": "",
        "Aptitudes7Cluster1": "",
        "Aptitudes8Cluster1": "",
        "Aptitudes9Cluster1": "",
        "Aptitudes10Cluster1": "",
        "Ocupaciones1Cluster2": "",
        "Ocupaciones2Cluster2": "",
        "Ocupaciones3Cluster2": "",
        "Ocupaciones4Cluster2": "",
        "Ocupaciones5Cluster2": "",
        "Ocupaciones6Cluster2": "",
        "Ocupaciones7Cluster2": "",
        "Ocupaciones8Cluster2": "",
        "Ocupaciones9Cluster2": "",
        "Ocupaciones10Cluster2": "",
        "Aptitudes1Cluster2": "",
        "Aptitudes2Cluster2": "",
        "Aptitudes3Cluster2": "",
        "Aptitudes4Cluster2": "",
        "Aptitudes5Cluster2": "",
        "Aptitudes6Cluster2": "",
        "Aptitudes7Cluster2": "",
        "Aptitudes8Cluster2": "",
        "Aptitudes9Cluster2": "",
        "Aptitudes10Cluster2": "",
        "TerminosCC": "1"
    },
    {
        "PortfolioID": "",
        "MMDate": "06/17/2014",
        "Cluster1": "Ciencias Humanas",
        "Cluster2": "Ciencias de la Salud",
        "ResultURL": "https://www2.careercruising.com/Default/Laureate?PortfolioId=",
        "PhoneNumber": "33445566",
        "Ocupaciones1Cluster1": "",
        "Ocupaciones2Cluster1": "",
        "Ocupaciones3Cluster1": "",
        "Ocupaciones4Cluster1": "",
        "Ocupaciones5Cluster1": "",
        "Ocupaciones6Cluster1": "",
        "Ocupaciones7Cluster1": "",
        "Ocupaciones8Cluster1": "",
        "Ocupaciones9Cluster1": "",
        "Ocupaciones10Cluster1": "",
        "Aptitudes1Cluster1": "",
        "Aptitudes2Cluster1": "",
        "Aptitudes3Cluster1": "",
        "Aptitudes4Cluster1": "",
        "Aptitudes5Cluster1": "",
        "Aptitudes6Cluster1": "",
        "Aptitudes7Cluster1": "",
        "Aptitudes8Cluster1": "",
        "Aptitudes9Cluster1": "",
        "Aptitudes10Cluster1": "",
        "Ocupaciones1Cluster2": "",
        "Ocupaciones2Cluster2": "",
        "Ocupaciones3Cluster2": "",
        "Ocupaciones4Cluster2": "",
        "Ocupaciones5Cluster2": "",
        "Ocupaciones6Cluster2": "",
        "Ocupaciones7Cluster2": "",
        "Ocupaciones8Cluster2": "",
        "Ocupaciones9Cluster2": "",
        "Ocupaciones10Cluster2": "",
        "Aptitudes1Cluster2": "",
        "Aptitudes2Cluster2": "",
        "Aptitudes3Cluster2": "",
        "Aptitudes4Cluster2": "",
        "Aptitudes5Cluster2": "",
        "Aptitudes6Cluster2": "",
        "Aptitudes7Cluster2": "",
        "Aptitudes8Cluster2": "",
        "Aptitudes9Cluster2": "",
        "Aptitudes10Cluster2": "",
        "TerminosCC": "1"
    }
]


def load_clusters(directory):
    COL_CODE = 0
    COL_NAME = 1
    COL_NAME_ES = 2
    COL_NAME_MX = 3
    COL_NAME_CL = 4
    COL_NAME_PE = 5
    COL_NAME_EC = 6
    COL_NAME_BR = 7

    data_file = os.path.join(directory, 'clusters.csv')

    with open(data_file, 'rb') as csvfile:
        clusterreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in clusterreader:
            clusters[row[COL_CODE]] = {
                "code": row[COL_CODE],
                "name": row[COL_NAME],
                "name_es": row[COL_NAME_ES],
                "name_mx": row[COL_NAME_MX],
                "name_cl": row[COL_NAME_CL],
                "name_pe": row[COL_NAME_PE],
                "name_ec": row[COL_NAME_EC],
                "name_br": row[COL_NAME_BR]
            }


def load_occupations(directory):
    COL_CODE = 0
    COL_NAME = 1
    COL_NAME_ES = 2
    COL_CLUSTERS = 3
    COL_DESCRIPTION = 4

    data_file = os.path.join(directory, 'occupations.csv')

    with open(data_file, 'rb') as csvfile:
        clusterreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in clusterreader:
            occupations[row[COL_CODE]] = {
                "code": row[COL_CODE],
                "name": row[COL_NAME],
                "name_es": row[COL_NAME_ES],
                "clusters": row[COL_CLUSTERS],
                "description": row[COL_DESCRIPTION]
            }


def load_occupations_by_country(directory):
    COL_CODE = 0
    COL_NAME = 1

    countries_list = countries.keys()

    countries_list.remove("hn")
    countries_list.remove("us")

    for country in countries_list:
        data_file = os.path.join(directory, 'occ_{0}.csv'.format(country))

        with open(data_file, 'rb') as csvfile:
            clusterreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in clusterreader:
                occupations[row[COL_CODE]]["name_%s" % country] = row[COL_NAME]


def init(directory):
    load_clusters(directory)

    load_occupations(directory)

    load_occupations_by_country(directory)
