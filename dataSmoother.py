import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

import csv
secondsList = []
altitudeList = []
smoothedData = []

line = 0
with open('trimmedData.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        if line != 0:
            secondsList.append(row[1])
            altitudeList.append(float(row[2]))
        line = line + 1

for i in range(5, len(secondsList)-5):
    meanValue = (altitudeList[i-2] + altitudeList[i-1] + altitudeList[i] + altitudeList[i+1] + altitudeList[i+2])/5
    smoothedData.append([secondsList[i], meanValue])

print(smoothedData)

with open('smoothedData.csv', mode='w', newline='') as smoothedCSV:
    csvWriter = csv.writer(smoothedCSV, delimiter=',')
    for row in smoothedData:
        csvWriter.writerow(row)