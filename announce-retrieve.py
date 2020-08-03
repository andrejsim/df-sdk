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

    metadata = {
        "datasetname": "wavewatch_global_30min",
        "datafiletype": "netcdf",
        "datafilename":
            "201906270600/mg/wavewatch/global/30min/st2/gfs/wavewatch_global_30min_st2_gfs_fields_20190627_0600_t0m1.nc",
        "parameters": ["t0m1"],
        "timeframe": {
            "issuetime": "2019-06-27T09:42:28Z",
            "validtime": ["2019-06-27T09:00:00.000Z"],
            "step": ["30m"]
        },
        "source": {
            "ID": "s3://mg-metocean-processing-production-model-output",
            "description": "mg-metocean-processing-production-model-output"
        },
        "process": {
            "ID":
                "github.com/MeteoGroup/hpc-suites",
            "description":
                "WST Nautical hpc-suites repo. s3://configuration bucket."
        },
    }

    success, dataid = df.announceAndUpload(
        metadata, "README.md")
    print(f"{success}, {dataid}")

    if success:
        resp = df.downloadDataID(dataid, "/tmp/output.md")
        pp(resp)

        pp(df.queryDataID(dataid))
