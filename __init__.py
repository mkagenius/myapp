import os
import requests 
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, render_template, flash, request
from werkzeug.utils import secure_filename

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
#        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    SECRET_KEY='dev'
    headers = {'Content-type': 'application/json'}
    headers['Authorization'] = 'Bearer ' + SECRET_KEY
    #if test_config is None:
        # load the instance config, if it exists, when not testing
     #   app.config.from_pyfile('config.py', silent=True)
    #else:
        # load the test config if passed in
     #   app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/level1')
    def level1():
        servers = ['http://178.128.69.227/stats', 'http://206.189.12.5/stats'] 
        response = requests.get("https://api.digitalocean.com/v2/droplets", headers=headers)        
        j = json.loads(response.text)
        droplets_list = j['droplets']
        name_vol_list = []
        for s in servers:
            val = requests.get(s)
            z = val.text.split()
            speed = z[0]
            free = z[1]
            name_vol_list.append([s.split('/')[2], speed, free])

        return render_template('level1.html', droplets=name_vol_list)

    @app.route('/level2')
    def level2():
        servers = ['http://178.128.69.227/stats', 'http://206.189.12.5/stats']
        response = requests.get("https://api.digitalocean.com/v2/droplets", headers=headers)
        j = json.loads(response.text)
        droplets_list = j['droplets']
        name_vol_list = []
        for s in servers:
            val = requests.get(s)
            z = val.text.split()
            speed = z[0]
            free = z[1]
            name_vol_list.append([s.split('/')[2], speed, free])

        return render_template('level1.html', droplets=name_vol_list)
                
		
    return app

