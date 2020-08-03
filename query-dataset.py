from os import getenv

import datafabric

if __name__ == "__main__":
    apikey = getenv("DF_APIKEY")
    apiurl = getenv("DF_APIURL")

    df = datafabric.Datafabric(apiurl,
                               apikey,
                               log_format=None,
                               user_agent="sdk-example/0.2")  # required

    dataid = "7cf9e8c5-1397-4616-b9d1-848afe4afbc5"
    datafabric.display_response(df.queryDataID(dataid))

    terms = {"provided.datasetname": "scado", "provided.timeframe.issuetime": "2019-12-01T09:00:00Z"}
    resp = df.query(terms)
    datafabric.display_response(resp)

    resp = df.query_terms(dataset="scado", issuetime="2019-12-01T09:00:00Z")
    datafabric.display_response(resp)

    dataid = resp[0]['data']['items'][0]['dataID']

    datafabric.display_response(df.queryDataID(dataid))
