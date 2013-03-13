#-*- coding:utf-8 -*-

import datetime

from flask import render_template

from leaf import app
from leaf.models.user_model import User

@app.route('/hello',methods=['GET'])
def hello():
    User.create('123456', 'huangxin', 'huangxin@douban.com', datetime.datetime.now(), '')
    User.query_obj.get_by_username('huangxin').set_email('huangxinms@gmail.com')
    print User.query_obj.get_by_username('huangxin').get_email()
    return render_template('hello.html')
