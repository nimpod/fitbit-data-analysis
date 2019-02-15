import json
import pandas as pd

def readJSON(filePath):
    with open(filePath, 'r') as f:
        return json.load(f)


def getDate(dateTime):
    dateTimeArray = dateTime.split()
    return dateTimeArray[0]


def convertToMDY(date):
    dateParts = date.split("-")
    year = dateParts[0]
    month = dateParts[1]
    day = dateParts[2]
    return '{}/{}/{}'.format(month, day, year[2:])


def extractDayData(specifiedDate, specifiedData, rawData, divisor):
    dailySum = 0
    oldDate = specifiedDate

    for obj in rawData['data']:
        newDate = getDate(obj['dateTime'])
        if (specifiedData == 'calories'):
            dataValue = float(obj['value'])
        else:
            dataValue = int(obj['value'])
        
        if (oldDate == newDate):
            dailySum += dataValue
            oldDate = getDate(obj['dateTime'])
        else:
            dailySum /= divisor
            return round(dailySum)

def extractMonthOfData(startDate):
    stepData = readJSON('../../user-site-export/steps-' + startDate + '.json')
    distanceData = readJSON('../../user-site-export/distance-' + startDate + '.json')
    altitudeData = readJSON('../../user-site-export/altitude-' + startDate + '.json')
    caloriesData = readJSON('../../user-site-export/calories-' + startDate + '.json')

    daterange = pd.date_range(startDate, periods=31)

    for date in daterange:
        fileDate = getDate(str(date))
        jsonDate = convertToMDY(fileDate)
        
        steps = extractDayData(jsonDate, 'steps', stepData, divisor=1)
        distance = extractDayData(jsonDate, 'distance', distanceData, divisor=100000)
        altitude = extractDayData(jsonDate, 'altitude', altitudeData, divisor=10)
        calories = extractDayData(jsonDate, 'calories', caloriesData, divisor=1)
        

writeJSON('health-data.json')
extractMonthOfData('2019-01-10')