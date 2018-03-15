# -*- coding: utf-8 -*-
from __future__ import print_function
"""
    package.module
    ~~~~~~~~~~~~~~

    控制层首页模块

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""

import sys

from flask import Blueprint, render_template, session
from modules import users

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

b_index = Blueprint('b_index', __name__)

user = users.Users()

@b_index.route('/')
@b_index.route('/index')
@users.is_login
def index():
    '''首页'''

    username = session['username'] # 过登陆装饰器所以不用验证
    signed = user.today_is_sign(user.get_uid(username))

    return render_template('index.html', signed=signed)