# -*- coding: utf-8 -*-
from flask import Module

app = Module(__name__, 'admin', url_prefix='/admin')
