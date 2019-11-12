# Import packages
import requests
import datetime
import base64

# API credentials and database credentials
API_KEY = ''
API_SECRET = ''
AUTHORISATION_TOKEN = ''
HOST = ''
USER = ''
PASSWD = ''
AUTH_PLUGIN = ''

# Specify 'PRODUCTION' or 'DEVELOPMENT
RUNNING_MODE = 'DEVELOPMENT'

# Get variables from `private.py` or `private_test.py`
if RUNNING_MODE == 'PRODUCTION':
    try:
        from private import *
    except:
        pass
elif RUNNING_MODE == 'DEVELOPMENT':
    try:
        from private_development import *
    except:
        pass

# Helper functions
def current_time():
    return datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S %p')

def current_date():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def get_access_token(key=API_KEY, 
                     secret=API_SECRET,
                     token=AUTHORISATION_TOKEN):
    authorisation = base64.b64encode(str.encode(key + ':' + secret))
    headers = {'Authorization': authorisation}
    response = requests.get('https://api.onegov.nsw.gov.au/oauth/client_credential/accesstoken?grant_type=client_credentials', headers=headers)
    return 'Bearer ' + response.json()['access_token']

# Set access token and headers
AUTHORISATION_TOKEN = get_access_token()
headers = {'apikey': API_KEY,
           'transactionid': current_time(),
           'requesttimestamp': current_time(),
           'Content-Type': 'application/json; charset=utf-8',
           'Authorization': AUTHORISATION_TOKEN}





