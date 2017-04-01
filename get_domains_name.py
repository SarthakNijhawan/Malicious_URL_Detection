#!/usr/bin/python

from urllib.parse import urlparse

import numpy as np
import pandas as pd

allurls = '/home/vikrant/tmp/data.csv'  # path to our all urls file
allurlscsv = pd.read_csv(allurls, ',', error_bad_lines=False)  # reading file
allurlsdata = pd.DataFrame(allurlscsv)  # converting to a dataframe
allurlsdata = np.array(allurlsdata)  # converting it into an array


for url in allurlsdata:
    if url[0].startswith("http://"):
        hostname = urlparse(url[0]).hostname
        print(hostname)
        # if hostname is None:
        #     print(url[0])
