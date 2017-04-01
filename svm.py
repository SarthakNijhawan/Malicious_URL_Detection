import pandas as pd
from sklearn.svm import SVC


def ip_to_binary(ip):
    ip_str = ''.join([bin(int(x) + 256)[3:] for x in ip.split('.')])
    return list(map(int, list(ip_str)))


all_urls = 'final2.csv'  # path to our all urls file
all_urls_csv = pd.read_csv(all_urls, ',', error_bad_lines=False)  # reading file

all_urls_with_ip = all_urls_csv[all_urls_csv['ip'] != 'None']

X = []
Y = []
for index, row in all_urls_with_ip.iterrows():
    url, ip, y = row['url'], row['ip'], row['y']
    x = ip_to_binary(ip)
    if y == "bad":
        y = -1
    else:
        y = 1
    X.append(x)
    Y.append(y)
clf = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, max_iter=-1, probability=True, random_state=None,
          shrinking=True, tol=0.001, verbose=False)
clf.fit(X, Y)
