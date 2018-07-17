import datetime, re, os
from pandas import Series, DataFrame
from flask import Flask
from inputs.settings import *
import requests
#from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/SportPoll/vote/<Sport>')
def SportPoll(Sport=None):
    t = DataFrame({'sport':[str(Sport)]})
    try:
        SportList = DataFrame.from_csv('data/SportPoll.csv')
        SportList = SportList.append(t, ignore_index=True)
    except:
        SportList = t
    SportList.to_csv('data/SportPoll.csv')
    r = DataFrame(SportList['sport'].value_counts())
    return r.to_html(border=0)

@app.route('/who')
def who():
    url = "https://api.meraki.com/api/v0/organizations"

    headers = {
       'cache-control': "no-cache",
       'x-cisco-meraki-api-key': MERAKI_KEY
       }
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers)

    r = response.text

    return r
