import bottle
from bottle import Bottle, run, \
     template, debug, static_file

import os, sys


dirname = os.path.dirname(sys.argv[0]) + '\\eve_web_fw\\'

app = Bottle()
debug(True)
bottle.TEMPLATE_PATH.insert(0,dirname)
bottle.TEMPLATE_PATH

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/asset/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'/static/asset/js')

@app.route('/')
def index():
    data = {"developer_name":"Ikram Shariff",
            "developer_organization":"spacegoat"}
    return template('views//template//index', data = data)

if __name__ == '__main__':
    run(app,host='localhost', port=8080, debug=True)