# --------------
# Prerequisite
# --------------
# If you have not already installed the requests package and/or the json package 
# a. pip install requests
# b. pip install json

import requests
import json

# --------------
# Step 1 - Update this URL with your domain endpoint
# --------------
os_url = 'https://search-fluentd-domain-qjskzejtju5tryntaw6s4wkbfa.us-east-1.es.amazonaws.com'

# --------------
# Step 2 - Update ARN of IAM role to map to OpenSearch all_access role
# --------------

iam_arn = 'arn:aws:iam::376390845435:user/Fluentd_User_OpenSearch'

# --------------
# Step 3 - Map IAM user ARN to all_access role
# --------------
request_body = {
	"backend_roles" : [ "all_access"],
	"users" : [ '"' + iam_arn + '"', "OSMasterUser"]
}	

map_user_r = requests.put(os_url + '/_plugins/_security/api/rolesmapping/all_access', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(request_body))

print(map_user_r.text)