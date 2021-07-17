# -*- coding: utf-8 -*-
# @Time    : 09.05.21 19:09
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @Web     : http://tekrajchhetri.com/
# @File    : run.py
# @Software: PyCharm

from app import app
from db import db
db.init_app(app)
with app.app_context():
    db.create_all()
    print("Running")
app.run(host ='0.0.0.0', port = 5001, debug=False)
