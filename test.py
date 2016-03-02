from flask import Flask, url_for, Response
import flask
import json
import requests
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

app = Flask(__name__)

npmres = {
        'sendmms': True,
        'showauthurl': False,
        'authstate': None,
        'text': "Please work",
        'speech': "please speak",
        'status': "OK",
        'webhookreply': None, 
        'images': [
            {
                'imageurl': "http://api.dev.promptapp.io/images/random/helloworld.gif", 
                'alttext': "Hello World!"
                }
            ]
        }

target = 'https://api.dev.promptapp.io/api/1.0/webhook/@test101_00026'
head={'Content-Type': 'application/json'} 
head['Prompt-API-key']='7adde7aba673f3d7f382f2d59b41ffd5'
payload = {'message': 'Not too sure'}
payload['uuid']="517c843897fd4411b70ab3256e39f9da60b14483f0b2893e268fe12d57ac09d1"

OUR_API_KEY = '7adde7aba673f3d7f382f2d59b41ffd5' 

def checkIfRequestFromPrompt(inp):
    return inp==OUR_API_KEY or True

seen={}
def validate(command, uid):
    feedback = "No feedback"
    return True, feedback

def createResult(feedback):
    res = dict(npmres)
    res['message']=feedback
    return res

def jarvis(inp):
    mes = inp['message']
    uid = inp['uuid']

    res, feedback = validate('message', uid)
    if res is not True:
        return createResult(feedback)
    else:
        return createResult("Received: "+inp['message'])

@app.route('/', methods=['POST', 'GET'])
def api_root():
    f=open('newfile', 'w')
    f.write('Hello. THis thing works')
    f.close()
    print flask.request
    d = flask.request.data
    h = flask.request.headers
    if False:
        for i in h:
            a,b = i
        print a, b
        if a.lower() == 'Prompt-Api-Key'.lower():
            if not checkIfRequestFromPrompt(b):
                print 'Unauthorized access . . .'
                return

    dic = json.loads(d)

    ans = npmres
    ans=jarvis(dic)
    print ans

    return json.dumps(ans)


resp={"ok":"okk"}
@app.route('/code', methods=['POST', 'GET'])
def api_code():
    f=open('newfile', 'r')
    print f.read()
    print flask.request, type(flask.request)
    return json.dumps(resp)

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2564)

'''
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials(clientID = 'client0'):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    # home_dir = os.path.expanduser('~')
    credential_dir = os.path.join('..', 'credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   clientID+'.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_events(day = 'tomorrow'):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    UTC_OFFSET_TIMEDELTA = datetime.datetime.utcnow() - datetime.datetime.now()

    date = datetime.datetime.utcnow()#.isoformat() + 'Z' # 'Z' indicates UTC time
    if day == 'tomorrow':
        date += datetime.timedelta(days=1)

    start_date = datetime.datetime(date.year, date.month, date.day) + UTC_OFFSET_TIMEDELTA + datetime.timedelta(0,1)
    end_date = start_date + datetime.timedelta(days=1) - datetime.timedelta(0,1)
    start_date = start_date.isoformat() + 'Z'
    end_date = end_date.isoformat() + 'Z'
    #print(start_date, end_date)

    #print('Getting the upcoming events for the day')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=start_date, timeMax=end_date, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    schedule_dict = {}
    for event in events:
        event_dict = {}

        time = event['start'].get('dateTime')[11:19]
        event_dict['time'] = time

        if 'summary' in event.keys():
            event_dict['summary'] = event['summary']

        if 'location' in event.keys():
            event_dict['location'] = event['location']

        schedule_dict[time] = event_dict

    return schedule_dict


def main():
    get_events()

if __name__ == '__main__':
    main()
'''
