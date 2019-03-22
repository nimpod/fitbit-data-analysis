import json
import csv
import pandas
from FitbitDate import FitbitDate

# read contents of a json file
def readJSON(filePath):
    with open(filePath, 'r') as f:
        return json.load(f)


# get the Date only from dateTime in the JSON files
def getDate(dateTime):
    dateTimeArray = dateTime.split()
    return dateTimeArray[0]


# extract one days worth of health data
def extractDailyData(keyDate, specifiedData, rawData, divisor):
    dailySum = 0

    for obj in rawData['data']:
        month, day, year = getDate(obj['dateTime']).split("/")
        currentDate = FitbitDate('20'+year, month, day)
        dataValue = float(obj['value'])
        
        #print(obj, currentDate.toMDYWithSlash(), keyDate.toMDYWithSlash(), specifiedData, dataValue, dailySum, (obj['dateTime'] == rawData['data'][-1]['dateTime']))

        # we are ahead, or file ended
        if ((currentDate.toYMDWithHyphen() > keyDate.toYMDWithHyphen()) or (obj['dateTime'] == rawData['data'][-1]['dateTime'])):
            dailySum /= divisor
            return round(dailySum, 2) if (specifiedData == 'distance') else round(dailySum)

        # found the correct day, so count data
        elif (currentDate.toMDYWithSlash() == keyDate.toMDYWithSlash()):
            dailySum += dataValue

        # we are behind, so continue
        elif (currentDate.toYMDWithHyphen() < keyDate.toYMDWithHyphen()):
            continue


def extractMonthlyData(startDate):
    stepData = readJSON('../../Programming/user-site-export/steps-' + startDate + '.json')
    distanceData = readJSON('../../Programming/user-site-export/distance-' + startDate + '.json')
    altitudeData = readJSON('../../Programming/user-site-export/altitude-' + startDate + '.json')
    caloriesData = readJSON('../../Programming/user-site-export/calories-' + startDate + '.json')

    daterange = pandas.date_range(startDate, periods=30)

    for date in daterange:
        pdt = pandas.to_datetime(date)
        fileDate = pdt.date()

        year, month, day = str(fileDate).split("-")
        fitbitDate = FitbitDate(year, month, day)

        steps = extractDailyData(fitbitDate, 'steps', stepData, divisor=1)
        distance = extractDailyData(fitbitDate, 'distance', distanceData, divisor=100000)
        altitude = extractDailyData(fitbitDate, 'altitude', altitudeData, divisor=10)
        calories = extractDailyData(fitbitDate, 'calories', caloriesData, divisor=1)

        print(fileDate)

        dailyData = [fileDate, steps, distance, altitude, calories]

        with open('health-data.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(dailyData)
            #print('wrote data from ' + fileDate + ' to csvfile')    


# extract all data between 2017-06-19 and 2019-01-10
def extractAllData():
    months = pandas.date_range(start='2017-06-19', end='2019-01-10', periods=570)
    for i in range(len(months)):
        if (i % 30 == 0):
            extractMonthlyData(getDate(str(months[i])))


#extractAllData()
