import json

def getJSON(filePath):
    with open(filePath, 'r') as f:
        return json.load(f)

def getDateFromDateTime(dateTime):
    dateTimeArray = dateTime.split()
    return dateTimeArray[0]

def maxDataInterval(specifiedData, specifiedDate):
    jsonData = getJSON('../../user-site-export/' + specifiedData + '-' + specifiedDate + '.json')
    max = 0
    for item in jsonData['states']:
        steps = int(item['value'])
        if (steps >= max):
            max = steps
            datetime = item['dateTime']
    return (max, datetime)
        

'''
{
  "date" : "01/10/01",
  "steps" : 17872,
  "distance" : 6883,
  "altitude" : 64,
  "calories" : 4351
}

# print(len(data['states']))
dailyData = dict()

def extractDates(specifiedDate):
    data = getJSON('../../user-site-export/steps-' + specifiedDate + '.json')
    for date in data['states']:
        dailyData['date'] = getDateFromDateTime(date['dateTime'])
    
    with open('all_health_data.json', 'w') as f:
        json.dump(dailyData, f)

def extractRawData(specifiedData, specifiedDate):
    data = getJSON('../../user-site-export/' + specifiedData + '-' + specifiedDate + '.json')
    oldDateTime = specifiedDate
    dailyDataSum = 0

    for item in data['states']:
        newDateTime = getDateFromDateTime(item['dateTime'])
        dataInterval = int(item['value'])

        # we got to the end of a day
        if (oldDateTime != newDateTime):
            dailyData[specifiedData] = dailyDataSum
            print(json.dumps(dailyData, indent=2))

            with open('all_health_data.json', 'w') as f:
                json.dump(dailyData, f)
            dailyDataSum = 0
        
        dailyDataSum += dataInterval
        oldDateTime = getDateFromDateTime(item['dateTime'])

# extractDates('2019-01-10')
extractRawData('steps', '2019-01-10')
#print(json.dumps(dailyData, indent=2))
#print(maxDataInterval('steps', '2019-01-10'))

'''