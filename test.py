from flask import Flask, url_for, Response
import flask
import json
import requests
app = Flask(__name__)

dat = {
            "id": 1,
            "sendmms": False,
            "showauthurl": False,
            "text" : "Please work",
            "speech" : "Please please work",
            "status" : "OK",
                "name": "This stuff is online",
                    "price": 12.50,
                        "tags": ["home", "green"]
                        }

target = 'https://api.dev.promptapp.io/api/1.0/webhook/@test101_00026'
headers = {'content-type': 'application/json'}
headers['Prompt-API-key']='26e805e78f0d8ca28098c14077500a42'
payload = {'some': 'data'}
payload['uuid']="517c843897fd4411b70ab3256e39f9da60b14483f0b2893e268fe12d57ac09d1"


@app.route('/', methods=['POST', 'GET'])
def api_root():
    print request.method

    d = flask.request.data
    print d
    datadict = json.loads(d)
    if datadict['prerequisites']['shippingaddress']['state']:
        res=datadict['prerequisites']['shippingaddress']['state']
        dat['returnans']=res*4
    else:
        print '....\n...\nNOT FOUND\n\n'
    tt = flask.jsonify(**dat)
    print type(tt)

    #r=requests.post(target, json.dumps(payload), headers=headers)
    #print r.content

    res = flask.Response("Foo Bar")
    res.headers['Prompt-API-key']='26e805e78f0d8ca28098c14077500a42'
    res.headers['content-type'] = 'application/json'

    return tt

@app.route('/articles')

def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


if __name__ == '__main__':
    app.run()


