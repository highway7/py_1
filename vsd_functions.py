import urllib.request
import json
import base64

import getVSDKey

def addDomain(vpn_name):
    authkey = getVSDKey.getVSDkey()

    headers = { 'X-Nuage-Organization': 'csp', \
                'Authorization': 'XREST ' + authkey, \
                'Content-Type': 'application/json'
    }

    null = None

    values = {
        "maintenanceMode": "DISABLED",
        "templateID": "f66df671-22e2-4584-bda9-a2de7f3f39a4",
        "customerID": null,
        "serviceID": null,
        "routeTarget": null,
        "routeDistinguisher": null,
        "description": "Python Test3",
        "name": vpn_name,
        "owner": null,
        "parentType": null,
        "parentID": null,
        "externalID": null,
        "ID": null
    }
 
    json_data = json.dumps(values)
    post_data = json_data.encode("utf-8")
        
    url = 'https://172.18.180.109:8443/nuage/api/v1_0/enterprises/31282ceb-7ef9-495a-998a-2a70e318cdc9/domains/'      
    req = urllib.request.Request(url, post_data, headers)
    resp = urllib.request.urlopen(req).read()
    data = json.loads(resp.decode('utf8'))
    
    return (data)

def getDomains(org_id):
    
    authkey = getVSDKey.getVSDkey()

    headers = { 'X-Nuage-Organization': 'csp', \
                'Authorization': 'XREST ' + authkey, \
                'Content-Type': 'application/json'
    }

    null = None
        
    url = 'https://172.18.180.109:8443/nuage/api/v1_0/enterprises/31282ceb-7ef9-495a-998a-2a70e318cdc9/domains'      
    req = urllib.request.Request(url, None, headers)
    resp = urllib.request.urlopen(req).read()
    data = json.loads(resp.decode('utf8'))
   
    return (data)

