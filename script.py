import pandas as pd

with open('export_raw.txt') as f:
    lines = f.readlines()

l = []
for line in lines:
    if line.strip():
        _ = line.strip().split("|")
        url = _[0]
        desc = ''.join(_[1:])
        l.append([url, desc])

df = pd.DataFrame(l, columns=['url', 'description'])
df.to_csv('export_csv.csv')