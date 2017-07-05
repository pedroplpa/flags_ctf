#!/usr/bin/env python
import json

from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

config = None

@app.route('/')
def index():
    # Render template
    render = render_template('main.html')
    return make_response(render)

@app.route('/', methods=['POST'])
def indexsubmit():
    try:
        userName = request.form['userName']
        userPassword = request.form['userPassword']
    except KeyError:
        pass
    else:
        if userName == "n0tth34dm1n" and userPassword == "uSbRuLeZ":
            message="TH1S_1S_H0W_Y0U_D0_1T{Y0U_4R3_4_H3LL_0F_4_W1NN3R}"
        else:
            message="Usuario ou senha incorretos"
        render = render_template('message.html', message=message)
        return make_response(render)



# Load config
config_str = open('config.json', 'rb').read()
config = json.loads(config_str)

app.secret_key = config['secret_key']

if config['isProxied']:
    app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    # Start web server
    app.run(host=config['host'], port=config['port'],
        debug=config['debug'], threaded=True)