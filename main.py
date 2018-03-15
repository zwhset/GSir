# -*- coding: utf-8 -*-
from __future__ import print_function
"""
    package.web
    ~~~~~~~~~~~~~~

    Gsir 启动入口

    :copyright: (supervisor.conf) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""
import sys

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

from flask import Flask

# main
app = Flask(__name__)
# Secret Key
app.config['SECRET_KEY'] = 'slkfjlweihow32j1ljnslafsfji32'

# 导入url 控制层
from controllers.users import b_users
from controllers.index import b_index

# 注册蓝图
app.register_blueprint(b_users)
app.register_blueprint(b_index)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8009, threaded=True, debug=True)