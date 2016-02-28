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

OUR_APP_KEY = '7adde7aba673f3d7f382f2d59b41ffd5' 


@app.route('/', methods=['POST', 'GET'])
def api_root():
    d = flask.request.data
    h = flask.request.headers
    print h
    print d

    #r=requests.post(target, json.dumps(payload), headers=head)

    return json.dumps(npmres)

@app.route('/articles')

def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


if __name__ == '__main__':
    app.run()


