import csv

# Open the CSV file
d1=open('example.csv', 'rb')
reader = csv.reader(d1)

 
d2=open('update_example.csv', 'wb')
writer = csv.writer(d2)
    
for row in reader:
    if row[0] == 'John Doe':
       row[1] = '3500'
    writer.writerow(row)