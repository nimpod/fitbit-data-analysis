import json
with open('../../user-site-export/steps-2019-01-10.json') as f:
    data = json.load(f)

def getDateFromDateTime(dateTime):
    dateTimeArray = dateTime.split()
    return dateTimeArray[0]

def maxStepsPerInterval():
    max = 0
    for item in data['states']:
        steps = int(item['value'])
        if (steps >= max):
            max = steps
            datetime = item['dateTime']

    return (max, datetime)

# print(len(data['states']))


dailySteps = dict()

oldDateTime = '01/10/19'
stepsInOneDay = 0

for item in data['states']:
    newDateTime = getDateFromDateTime(item['dateTime'])
    stepsInterval = int(item['value'])

    if (oldDateTime != newDateTime):
        dailySteps[stepsInOneDay] = oldDateTime
        stepsInOneDay = 0

    if (stepsInterval != 0):
        stepsInOneDay += stepsInterval

    oldDateTime = getDateFromDateTime(item['dateTime'])

print(json.dumps(dailySteps, indent=2))
print(maxStepsPerInterval())


















'''
people_string = 
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["js@gmail.com", "js@gmx.co.uk"],
            "has_license": false
        },
        {
            "name": "Jan Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

# data = json.loads(people_string)

''' GET EVERYONES NAME
--------------------------------
for person in data['people']:
    print(person['name'])
'''

''' DELETE EVERYONES PHONE NUMBER (requires converting from string to python object)
---------------------------------
for person in data['people']:
    del person['phone']

new_str = json.dumps(data, indent=2, sort_keys=True)        # dumps() converts strings to python objects. sort_keys is an optional parameter that sorts keys in alphabetical order
print(new_str)
'''

''' (load json files into python objects, and then write those objects back to json files)
--------------------------------

'''