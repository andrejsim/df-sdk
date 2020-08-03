from os import getenv

import datafabric

if __name__ == "__main__":
    apikey = getenv("DF_APIKEY")
    apiurl = getenv("DF_APIURL")

    df = datafabric.Datafabric(apiurl,
                               apikey,
                               log_format=None,
                               user_agent="sdk-example/0.2")  # required

    dataid = "024da8a4-1912-4d58-bb2b-9798f506ef26"
    datafabric.display_response(df.queryDataID(dataid))

    # dataset, limited
    dataset = "wavewatch_global_6min_st4_gfs"
    resp = df.query_terms(dataset=dataset)
    datafabric.display_response(resp)

    # dataset and issuetime
    dataset = "wavewatch_global_6min_st4_gfs"
    issuetime = "2019-12-02T06:00:00Z"
    resp = df.query_terms(dataset=dataset, issuetime=issuetime)
    datafabric.display_response(resp)

    # all
    dataset = "wavewatch_global_6min_st4_gfs"
    issuetime = "2019-12-02T06:00:00Z"
    validtime = "2019-12-11T12:00:00Z"

    resp = df.query_terms(dataset=dataset, issuetime=issuetime, validtime=validtime)
    datafabric.display_response(resp)
