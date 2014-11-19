# -*- coding: utf-8 -*-

import os
import csv

apps = {
    "local": "http://localhost:8080/_ah/api/bob/v3",
    "old": "https://3-dot-applied-area-757.appspot.com/_ah/api/bob/v3",
    "default": "https://3-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v3",
    "dev": "https://3-dot-api-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v3",
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
        "name": "Universiad Privada del Norte",
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
