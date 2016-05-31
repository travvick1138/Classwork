import json

"""

Format of the data.json

{    "locality": "Portland",
    "location": {
        "type": "Point",
        "coordinates": [-122.676207, 45.523452]

        }
    }

"""

f = open('data.json', 'r')
contents = f.read()
data = json.loads(contents)
f.close()

print('The Latitude/Longitude of {locality} is {lat}/{lon}.'.format(
    locality=data['locality'],
    lat=data['location']['coordinates'][1],
    lon=data['location']['coordinates'][0]


))