# -*- coding: utf-8 -*-

import os
import csv

apps = {
    "mockup": "http://private-c90e-bob15.apiary-mock.com",
    "gee": "https://bob-api-test.apigee.net/_ah/api/bob/v3",
    "local": "http://localhost:8080/_ah/api/bob/v1",
    "dev": "https://1-dot-applied-area-757.appspot.com/_ah/api/bob/v1",
    "qa": "https://1-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v1",
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
        "country": "hn"
    },
    {
        "code": "cc",
        "name": "Slingshot",
        "country": "us"
    },
    {
        "code": "unitec",
        "name": "Universidad Tecnológica Centroamericana",
        "country": "hn"
    },
    {
        "code": "ceutec",
        "name": "Centro Universitario Tecnológico",
        "country": "hn"
    },
    {
        "code": "upn",
        "name": "Universidad Privada del Norte",
        "country": "pe"
    },
    {
        "code": "cbs",
        "name": "CEDEPE Business School",
        "country": "br"
    },
]

clusters = {}

occupations = {}

completionupdate_results = [
    {
        "PortfolioID": "",
        "MMDate": "06/16/2014",
        "Cluster1": "SC",
        "Cluster2": "HE",
        "ResultURL": "https://www2.careercruising.com/Default/Laureate?PortfolioId=",
        "PhoneNumber": "22334455",
        "Ocupaciones1Cluster1": "151",
        "Ocupaciones2Cluster1": "13",
        "Ocupaciones3Cluster1": "57",
        "Ocupaciones4Cluster1": "266",
        "Ocupaciones5Cluster1": "450",
        "Ocupaciones6Cluster1": "201",
        "Ocupaciones7Cluster1": "",
        "Ocupaciones8Cluster1": "281",
        "Ocupaciones9Cluster1": "603",
        "Ocupaciones10Cluster1": "648",
        "Aptitudes1Cluster1": "D",
        "Aptitudes2Cluster1": "C",
        "Aptitudes3Cluster1": "D",
        "Aptitudes4Cluster1": "E",
        "Aptitudes5Cluster1": "D",
        "Aptitudes6Cluster1": "D",
        "Aptitudes7Cluster1": "D",
        "Aptitudes8Cluster1": "D",
        "Aptitudes9Cluster1": "D",
        "Aptitudes10Cluster1": "D",
        "Ocupaciones1Cluster2": "137",
        "Ocupaciones2Cluster2": "57",
        "Ocupaciones3Cluster2": "603",
        "Ocupaciones4Cluster2": "652",
        "Ocupaciones5Cluster2": "591",
        "Ocupaciones6Cluster2": "622",
        "Ocupaciones7Cluster2": "578",
        "Ocupaciones8Cluster2": "314",
        "Ocupaciones9Cluster2": "327",
        "Ocupaciones10Cluster2": "303",
        "Aptitudes1Cluster2": "C",
        "Aptitudes2Cluster2": "D",
        "Aptitudes3Cluster2": "D",
        "Aptitudes4Cluster2": "D",
        "Aptitudes5Cluster2": "D",
        "Aptitudes6Cluster2": "C",
        "Aptitudes7Cluster2": "C",
        "Aptitudes8Cluster2": "C",
        "Aptitudes9Cluster2": "C",
        "Aptitudes10Cluster2": "C",
        "TerminosCC": "1"
    },
    {
        "PortfolioID": "",
        "MMDate": "06/17/2014",
        "Cluster1": "BU",
        "Cluster2": "AR",
        "ResultURL": "https://www2.careercruising.com/Default/Laureate?PortfolioId=",
        "PhoneNumber": "33445566",
        "Ocupaciones1Cluster1": "65",
        "Ocupaciones2Cluster1": "545",
        "Ocupaciones3Cluster1": "259",
        "Ocupaciones4Cluster1": "172",
        "Ocupaciones5Cluster1": "128",
        "Ocupaciones6Cluster1": "362",
        "Ocupaciones7Cluster1": "615",
        "Ocupaciones8Cluster1": "380",
        "Ocupaciones9Cluster1": "354",
        "Ocupaciones10Cluster1": "353",
        "Aptitudes1Cluster1": "D",
        "Aptitudes2Cluster1": "C",
        "Aptitudes3Cluster1": "D",
        "Aptitudes4Cluster1": "E",
        "Aptitudes5Cluster1": "D",
        "Aptitudes6Cluster1": "D",
        "Aptitudes7Cluster1": "D",
        "Aptitudes8Cluster1": "D",
        "Aptitudes9Cluster1": "D",
        "Aptitudes10Cluster1": "D",
        "Ocupaciones1Cluster2": "290",
        "Ocupaciones2Cluster2": "394",
        "Ocupaciones3Cluster2": "349",
        "Ocupaciones4Cluster2": "296",
        "Ocupaciones5Cluster2": "104",
        "Ocupaciones6Cluster2": "633",
        "Ocupaciones7Cluster2": "351",
        "Ocupaciones8Cluster2": "28",
        "Ocupaciones9Cluster2": "37",
        "Ocupaciones10Cluster2": "142",
        "Aptitudes1Cluster2": "C",
        "Aptitudes2Cluster2": "D",
        "Aptitudes3Cluster2": "D",
        "Aptitudes4Cluster2": "D",
        "Aptitudes5Cluster2": "D",
        "Aptitudes6Cluster2": "C",
        "Aptitudes7Cluster2": "C",
        "Aptitudes8Cluster2": "C",
        "Aptitudes9Cluster2": "C",
        "Aptitudes10Cluster2": "C",
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
