# -*- coding: utf-8 -*-
from accounts import app

@app.route('/')
def index():
    return "Hello World!" 
