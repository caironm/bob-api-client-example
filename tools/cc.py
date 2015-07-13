#!/usr/bin/env python
# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from cc_fns import load_clusters
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

    clusters = load_clusters(wb)

    pprint.pprint(clusters)
