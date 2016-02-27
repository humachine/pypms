from flask import Flask, url_for, Response
import flask
import json
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

@app.route('/', methods=['POST'])
def api_root():
    d = flask.request.data
    datadict = json.loads(d)
    res=datadict['prerequisites']['shippingaddress']['state']
    dat['returnans']=res*4
    tt = flask.jsonify(**dat)
    return tt

@app.route('/articles')

def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


if __name__ == '__main__':
    app.run()


