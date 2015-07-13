#!/usr/bin/env python
# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from cc_fns import load_clusters, load_occupations, country_codes
from cc_fns import clusters_sheet_name, occupations_sheet_names
import argparse
import pprint


parser = argparse.ArgumentParser()

parser.add_argument(
    "-f", "--filename",
    type=str,
    help="Portfolio ID to be confirmed")


if __name__ == "__main__":
    args = parser.parse_args()

    wb = load_workbook(args.filename)

    print('Sheet names: %s' % str(wb.get_sheet_names()))

    clusters = load_clusters(wb, clusters_sheet_name)

    pprint.pprint(clusters)

    postfix = 'mx'

    occupations = {}

    for country in country_codes:
        occupations = load_occupations(
            wb, occupations_sheet_names[country], country,
            occupations)

    pprint.pprint(occupations)
