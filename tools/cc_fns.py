# -*- coding: utf-8 -*-

clusters_sheet_name = "ClusterCodes"

occupations_sheet_names = {
    'mx': 'Mexico',
    'cl': 'Chile',
    'pe': 'Peru',
    'ec': 'Ecuador',
    'br': 'Brazil'
}

country_codes = [
    'mx', 'cl', 'pe', 'ec', 'br'
]

def load_clusters(wb, sheet_name):
    clusters = {}

    ws = wb[sheet_name]

    country_postfixes = {
        "CCClusters": "",
        "ChileClusters": "cl",
        "EcuadorClusters": "ec",
        "MexicoClusters": "mx",
        "PeruClusters": "pe",
        "BrazilClusters": "br"
    }

    for row in ws.rows[1:]:
        code = row[1].value
        name = row[2].value
        clusterType = row[3].value
        name_local = row[4].value

        if clusterType in country_postfixes:
            local_postfix = country_postfixes[clusterType]

            if code not in clusters:
                clusters[code] = {}

            clusters[code]["code"] = code

            if local_postfix == "":
                clusters[code]["name"] = name
            else:
                clusters[code]["name_%s" % local_postfix] = name_local

    return clusters

def load_occupations(wb, sheet_name, local_postfix, occupations):
    ws = wb[sheet_name]

    for row in ws.rows[1:]:
        code = row[0].value
        name_local = row[1].value
        name = row[2].value
        clusters = row[4].value.split(',') if row[4].value else []

        if code not in occupations:
            occupations[code] = {}

        occupations[code]["code"] = code

        if not "name" in occupations[code]:
            occupations[code]["name"] = name

        occupations[code]["name_%s" % local_postfix] = name_local

    return occupations
