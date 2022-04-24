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
os_url = 'https://search-workshop-domain-t67jt2mhmfhfv7mo3obcbczw4a.us-east-1.es.amazonaws.com'

# --------------
# Step 2 - Create the index
# --------------
create_index_r_body = {
  "settings": {
    "index": {
      "number_of_shards": 1,
      "number_of_replicas": 1
    }
  }, 
  "mappings": {
    "properties": {
      "eventtime" : {
        "type": "date",
        "format": "yyyy-MM-dd HH:mm:ss"
      },
      "application_id": {
        "type": "keyword"
      },
      "cpu_util": {
        "type": "integer"
      },
      "memory_util": {
        "type": "integer"
      },
      "disk_util": {
        "type": "integer"
      }
    }
  }
}

create_index_r = requests.put(os_url + '/alert-1', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(create_index_r_body))

print('------ Created an index on os cluster ------')
print(create_index_r.text)