import csv
import json
from collections import OrderedDict

def parse_csv(filename, delimiter=','):
    data = []

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)
        header = next(reader)

        for row in reader:
            tmp = OrderedDict()
            for k, v in zip(header, row):
                tmp[k] = v

            data.append(tmp)

    return data

def write_csv(filename, data, delimiter=','):
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=delimiter)

        for e,d in enumerate(data):
            if not e:
                writer.writerow(d.keys())

            writer.writerow(d.values())

data = parse_csv('new_file.csv')

for d in data:
    #print d
    if d['header1'] == 'data4':
        d['header2'] = "566gdss"

write_csv('data_updated.csv', data)

