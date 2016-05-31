






#Setup

def transform_timestamp_from_data_to_requested_format(timestamp):
    from datetime import datetime

    dt = datetime.fromtimestamp(timestamp)
    return '{dt.month}/{dt.day}/{dt.year}'.format(dt=dt)
#input
import urllib.request

handle = urllib.request.urlopen('http://api.randomuser.me/?results=5')
contents = handle.read()
text = contents.decode('utf-8')

import json

data = json.loads(text)


#Transform


#output
def main():

    for person in data['results']:
        print("""    Name: {title} {first} {last}
    Email: {email}
    Username: {username}
    Registration date: {regdate}
    Date of Birth: {bdate}
    """.format(
            title=person['name']['title'].title(),
            first=person['name']['first'].title(),
            last=person['name']['last'].title(),
            email=person['email'],
            username=person['login']['username'],
            regdate=transform_timestamp_from_data_to_requested_format(person['registered']),
            bdate=transform_timestamp_from_data_to_requested_format(person['dob'])
        ))
main()