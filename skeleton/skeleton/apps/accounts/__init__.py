# -*- coding: utf-8 -*-
from flask import Module

app = Module(__name__, 'accounts', url_prefix='/accounts')
