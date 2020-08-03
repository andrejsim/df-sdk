from os import getenv

import datafabric

if __name__ == "__main__":
    apikey = getenv("DF_APIKEY")
    apiurl = getenv("DF_APIURL")

    df = datafabric.Datafabric(apiurl,
                               apikey,
                               log_format=None,
                               user_agent="sdk-example/0.2")  # required

    resp = df.query_terms(dataset="scado", issuetime="2019-12-01T09:00:00Z", parameters="TT")
    datafabric.display_response(resp)
