# -*- coding: utf-8 -*-
from flask import Flask
import os, sys

SECRET_KEY = '6RZ~Iz{*>a5R&ZX>s@>a*(H,rlaU*<hn1?{A5A7V/C9Z)lIB_xqmpe]^45}4*9|+L'

# where all our flask modules are place
APPS_DIR = "apps/"
# which modules should be loaded?
APPS = [ 'admin', 'accounts' ]
# absolute path to the project dir
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# are we in development environment?
DEV = True

def load_module(module_name):
    return __import__('%s.views' % module_name, fromlist="app").app

def create_app():
    app = Flask(__name__)
    
    if DEV:
        app.config.from_object('settings.Dev')
    else:
        app.config.from_object('settings.Prod')

    sys.path.append(os.path.join(BASE_DIR, APPS_DIR))

    for module_name in APPS:
        app.register_module(load_module(module_name))
    
    return app