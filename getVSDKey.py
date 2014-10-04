# The urllib2 module has been split across several modules in Python 3 named urllib.request and urllib.error.
import os
import django
import urllib.request
import urllib.error
import time
import datetime
import json
import base64

# Start execution here!
def getVSDkey():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tango.settings")
        
    # Set the request authentication headers
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d %H:%M:%S')
    headers = { 'X-Nuage-Organization': 'csp', \
             'Authorization': 'XREST Y3Nwcm9vdDpjc3Byb290'}
    
    # Send the GET request
    url = 'https://172.18.180.109:8443/nuage/api/v1_0/me/'      
    req = urllib.request.Request(url, None, headers)
    
    # Read the response
    resp = urllib.request.urlopen(req).read()
    data = json.loads(resp.decode('utf8'))
    apikey=data[0]['APIKey']
    username=data[0]['userName']
    authstr=username+":"+apikey
    authkey = (base64.b64encode(authstr.encode('utf-8')))
    authkey = authkey.decode("utf-8")
    return authkey



