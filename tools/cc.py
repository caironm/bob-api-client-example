#!/usr/bin/env python
# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from cc_fns import load_clusters, load_occupations, country_codes
from cc_fns import clusters_sheet_name, occupations_sheet_names
import argparse
import pprint


def load_all(filename):
    wb = load_workbook(filename)

    clusters = load_clusters(wb, clusters_sheet_name)

    occupations = {}

    for country in country_codes:
        occupations = load_occupations(
            wb, occupations_sheet_names[country], country,
            occupations)

    return (clusters, occupations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f", "--filename",
        type=str,
        help="Excel workbook filename")

    args = parser.parse_args()

    if args.filename:
        clusters, occupations = load_all(args.filename)

        pprint.pprint(clusters)

        pprint.pprint(occupations)

