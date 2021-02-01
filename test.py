import csv

data = []

with open('class130d1.csv', 'r') as f:
    csvReader = csv.reader(f)
    
    for row in csvReader:
        data.append(row)


NameData = []
DistanceData = []
Mass = []
Radius = []

Headers = ['NAME', 'Distance', 'Mass', 'Radius']

for i in range(1,len(data)):
    NameData.append(data[i][0])

for i in range(1,len(data)):
    DistanceData.append(data[i][1])

for i in range(1,len(data)):
    Mass.append(data[i][2])

for i in range(1,len(data)):
    Radius.append(data[i][9])

planet_Data = [NameData, DistanceData, Mass, Radius]  

with open('datasetfinal.csv','w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(Headers)
    csvWriter.writerows(planet_Data)