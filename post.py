import requests
response = requests.post('http://terumo-uat.apps.prod.nuxeo.io/nuxeo/api/v1/upload/', auth=('TISAdministrator', 'this!sapassw0rd4TISAdmin'))

print (response.text)