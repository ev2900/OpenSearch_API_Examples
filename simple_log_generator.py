import requests
import json

r = requests.get('https://search-workshop-domain-leader-hys2ht2mr672dsoh5s7m24zdbe.us-east-1.es.amazonaws.com/log-data-1/_doc/1', auth=('OSMasterUser', 'AwS#OpenSearch1'))

print(r.text)