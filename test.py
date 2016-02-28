from flask import Flask, url_for, Response
import flask
import json
import requests
app = Flask(__name__)

dat = {
            "sendmms": False,
            "showauthurl": False,
            "text" : "Please work",
            "speech" : "Please please work",
            "status" : "OK",
                        }
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

def jarvis(inp):
    if 'do' not in inp['message']:
        res = []
        res[:] = npmres[:]
        res['message'] = 'Invalid Input. Try again'
        return res
    if not True:
        r=requests.post(target, json.dumps(payload), headers=head)
    return npmres

    

@app.route('/', methods=['POST'])
def api_root():
    print 'Starting now'
    d = flask.request.data
    h = flask.request.headers
    print h, type(h)
    for i in h:
        a,b = i
        if a.lower() == 'Prompt-Api-Key'.lower():
            if not checkIfRequestFromPrompt(b):
                print 'Unauthorized access . . .'
                return

    dic = json.loads(d)
    print dic

    ans = npmres
    ans=jarvis(dic)

    return json.dumps(ans)

@app.route('/articles')

def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


if __name__ == '__main__':
    app.run()


