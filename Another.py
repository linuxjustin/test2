```py
from collections import OrderedDict

import csv
import json

def parse_csv(filename, delimiter=' '):
    data = []
 
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)
       
        for column in reader:
            if 'name' in column:
                break
 
        for row in reader:
            field = OrderedDict()
            for name, value in zip(column, row):
                field[name] = value

            data.append(field)

    return data

def write_csv(filename, data, delimiter=' '):
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=delimiter)

        for e,d in enumerate(data):
            if not e:
                writer.writerow(d.keys())

            writer.writerow(d.values())

def filter_and_count_field(data, field_name):
    result = [{field_name: d.get(field_name)} for d in data]
    result.append({'Count': len(result)})
    
    return result

data = parse_csv('data.csv')
data = filter_and_count_field(data, 'name')

write_csv('data_updated.csv', data)
```
