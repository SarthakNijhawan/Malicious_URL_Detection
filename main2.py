from urllib.parse import urlparse

import numpy as np
import pandas as pd
domain_ip_file = open("all_domain_ip.txt")
domain_ip_dict = {}
ip_asn_file = open("all_ip_asn.txt")
ip_asn_dict = {}
# ip - asn
for line in ip_asn_file:
    L = line.strip().split(' ')
    if len(L) == 2:
        ip, asn = L
        ip_asn_dict[ip] = asn
# domain - ip
for line in domain_ip_file:
    L = line.strip().split(' ')
    if len(L) == 2:
        domain, ip = L
        if ip in ip_asn_dict:
            domain_ip_dict[domain] = (ip, ip_asn_dict[ip])
        else:
            domain_ip_dict[domain] = (ip, None)
            # print(domain, ip)
    else:
        domain_ip_dict[domain] = (None, None)
        # domain - ip - asn
        # for key in domain_ip_dict:
        #     domain = key
        #     ip = domain_ip_dict[domain][0]
        #     asn = domain_ip_dict[domain][1]
        # print(domain, ip, asn)
# print(ip_asn_dict["1"])

all_urls = '/home/vikrant/tmp/data.csv'  # path to our all urls file
all_urls_csv = pd.read_csv(all_urls, ',', error_bad_lines=False)  # reading file
all_urls_data = pd.DataFrame(all_urls_csv)  # converting to a dataframe
all_urls_data = np.array(all_urls_data)  # converting it into an array


def get_domain(u):
    return u.split('/')[0]


for row in all_urls_data:
    url = row[0]
    y = row[1]
    if url.startswith("http://"):
        domain = urlparse(url).hostname
        url = "\"{}\"".format(url)
    else:
        domain = get_domain(url)
    try:
        ip = domain_ip_dict[domain][0]
        asn = domain_ip_dict[domain][1]
        print("{},{},{},{}".format(url, ip, asn, y))
    except:
        print("{},{},{},{}".format(url, None, None, y))
