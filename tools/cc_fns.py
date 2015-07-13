# -*- coding: utf-8 -*-

def load_clusters(wb):
    clusters = {}

    ws = wb["ClusterCodes"]

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
                clusters[code]["name_%s" % local_postfix] = name

    return clusters
