import csv

dataset1 = []
dataset2 = []

with open('DwarfPlanetData.csv', 'r') as f:
    csvReader = csv.reader(f)

    for row in csvReader:
        dataset1.append(row)

with open('datasetfinal.csv', 'r') as f:
    csvReader = csv.reader(f)

    for row in csvReader:
        dataset2.append(row)      

header1 = dataset1[0]
header2 = dataset2[0]

planetData1 = dataset1[1:]
planetData2 = dataset2[1:]

headers = ['NAME', 'Distance', 'Mass', 'Radius']

NewPlanetData = []

print(planetData1[1][0])
print(len(planetData1))

planet1Name = []
planet2Name = []

for i in range(len(planetData1)):
    planet1Name.append(planetData1[i][0])

for i in range(len(planetData2)):
    planet2Name.append(planetData1[i][0])

print(planet2Name)    

# for index,datarow in enumerate(planetData2):
#     NewPlanetData.append(planetData1[index] + planetData2[index])

# with open('Final.csv','w') as f:
#     csvWriter = csv.writer(f)
#     csvWriter.writerow(headers)
#     csvWriter.writerows(NewPlanetData)