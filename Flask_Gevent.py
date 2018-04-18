# coding: utf-8

from flask import Flask
from gevent import monkey
from gevent.pywsgi import WSGIServer
import time
from datetime import datetime
monkey.patch_all()

app = Flask(__name__)


@app.route('/author/<random>', methods=['GET', 'POST']) # <random> is the keypoint
def get_author(random): # rnadom is must
    print(datetime.now())
    print('get start...')
    time.sleep(10)
    return 'Allence'


if __name__ == '__main__':
    WSGIServer(('127.0.0.1', 8877), app).serve_forever()
