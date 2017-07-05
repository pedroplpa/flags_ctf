#!/usr/bin/env python
import json
import dataset
import subprocess


from flask import Flask
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import Response

from sqlalchemy import exc

app = Flask(__name__)

db = None
config = None

@app.route('/message')
def message():
    # Render template
    render = render_template('message.html')
    return make_response(render)

@app.route('/message', methods=['POST'])
def messagesubmit():
    try:
        message = request.form['message']
    except KeyError:
        return jsonify({'success':False})
    else:
        db.query("INSERT INTO messages (message) VALUES (:message)",message=message)
        render = render_template('sendOK.html')
        return make_response(render)

@app.route('/messagefrom')
def messagefrom():
    # Render template

    message = list(db.query("SELECT * FROM messages LIMIT 1"))
    if len(message) > 0:
        message = message[0]
        db.query("DELETE FROM messages WHERE id = :id",id=message["id"])
        text = message["message"]
    else:
        text=""

    render = render_template('messagefrom.html',message=text)
    return make_response(render)



# Load config
config_str = open('config.json', 'rb').read()
config = json.loads(config_str)

app.secret_key = config['secret_key']

app.jinja_env.autoescape = False

db = dataset.connect(config['db'])

if config['isProxied']:
    app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    # Start web server
    app.run(host=config['host'], port=config['port'],
        debug=config['debug'], threaded=True)