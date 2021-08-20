import json
import re
from csv import writer, DictWriter

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


with open('2057712.json') as json_file:
    jdata = json.load(json_file)
    jlist = list(jdata['data'])
    jlist2 =[]
    for u in jlist:
        u['title'] = striphtml(u['title'])
        keys_to_extract = ["rank_display", "title", "country", "score"]
        u2 = {key: u[key] for key in keys_to_extract}
        jlist2.append(u2)
              
csv_file = "data.csv"
csv_columns = ['rank_display', 'title', 'country', 'score']
try:
    with open(csv_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in jlist2:
            writer.writerow(data)
except IOError:
    print("I/O error")