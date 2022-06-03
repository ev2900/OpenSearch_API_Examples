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
os_url = '<domain endpoint URL>'

# Remove trailing slash if exists
os_url = os_url.strip().rstrip("/")

# --------------
# Step 2 - Update ARN of IAM role to map to OpenSearch all_access role
# --------------

iam_arn = '<IAM role/user ARN>'

# --------------
# Step 3 - Map IAM user ARN to all_access role
# --------------
request_body = {
	"users" : [iam_arn, "OSMasterUser"]
}	

map_user_r = requests.put(os_url + '/_plugins/_security/api/rolesmapping/all_access', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(request_body))

print(map_user_r.text)
