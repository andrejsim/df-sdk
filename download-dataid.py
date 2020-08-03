from os import getenv
from pprint import pprint as pp

import datafabric

if __name__ == "__main__":
    apikey = getenv("DF_APIKEY")
    apiurl = getenv("DF_APIURL")

    df = datafabric.Datafabric(apiurl,
                               apikey,
                               log_format=None,
                               user_agent="sdk-example/0.2")  # required

    # dataid = "8ba79342-e02a-4182-bcbf-58ed26aace70"  # scado
    dataid = "a62976c8-5147-4b69-a668-a5fdacf484f5"  # wavewatch

    pp(df.queryDataID(dataid))

    df.downloadDataID(dataid=dataid, filepath="/tmp/" + dataid, attempts=2)
