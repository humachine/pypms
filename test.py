from flask import Flask, url_for, Response
import flask
app = Flask(__name__)

dat = {
            "id": 1,
                "name": "This stuff is online",
                    "price": 12.50,
                        "tags": ["home", "green"]
                        }

@app.route('/', methods=['POST'])
def api_root():
    tt = flask.jsonify(**dat)
    print tt
    print type(tt)
    return tt

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


if __name__ == '__main__':
    app.run()


