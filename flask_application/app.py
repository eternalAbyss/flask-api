from flask import Flask
import threading
import logging

app = Flask(__name__)

@app.route('/')
def hello():
    return {'msg':'hello world!'}

@app.route('/thread')
def threading_count():
    logging.info("Number of threads running currently : {}".format(threading.active_count()))
    response = {
        'Current thread': str(threading.current_thread())
    }
    return response
