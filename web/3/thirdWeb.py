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

@app.route('/')
def index():
    # Render template
    render = render_template('main.html')
    return make_response(render)

@app.route('/', methods=['POST'])
def indexsubmit():
    subprocess.call("./db_script.sh")

    try:
        userPassword = request.form['userPassword']
    except KeyError:
        return jsonify({'success':False})
    else:
        try:
            queryDB = list(db.query('SELECT * FROM user WHERE pass = \"'+userPassword+'\"'))
        except exc.SQLAlchemyError as err:
            message = err
        else:
            if len(queryDB) > 0:
                message="Logado!"
            else:
                message="pass incorreto"
    render = render_template('message.html', message=message)
    return make_response(render)



# Load config
config_str = open('config.json', 'rb').read()
config = json.loads(config_str)

app.secret_key = config['secret_key']

# Connect to database
db = dataset.connect(config['db'])

if config['isProxied']:
    app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    # Start web server
    app.run(host=config['host'], port=config['port'],
        debug=config['debug'], threaded=True)