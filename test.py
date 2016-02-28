from flask import Flask, url_for, Response
import flask
import json
import requests
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

@app.route('/', methods=['POST'])
def api_root():
    print flask.request
    d = flask.request.data
    h = flask.request.headers
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

if __name__ == '__main__':
    app.run()


