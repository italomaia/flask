# -*- coding: utf-8 -*-
from admin import app

@app.route('/admin/')
def index():
    return "Hello Admin World!" 
