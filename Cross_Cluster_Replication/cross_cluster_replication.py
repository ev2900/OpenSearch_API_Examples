# --------------
# Prerequisite
# --------------
# If you have not already installed the requests package and/or the json package 
# a. pip install requests
# b. pip install json

import requests
import json
import datetime
import random

# --------------
# Step 1 
# --------------
# a. Navigate to OpenSearch page on the AWS console (https://console.aws.amazon.com/esv3/home?region=us-east-1#opensearch/domains/)
# b. Select the domain 'workshop-domain-follower'
# c. Select the connections tab under the 'workshop-domain-follower'
# d. Request an Outbound connections, under the drop down select 'workshop-domain-leader', name the connection (Connection alias) 'workshop-domain-leader'
# e. Navigate back to the OpenSearch page on the AWS console (https://console.aws.amazon.com/esv3/home?region=us-east-1#opensearch/domains/)
# d. Select the domain 'workshop-domain-leader'
# e. Select the connections tab under the 'workshop-domain-leader'
# f. Under the inbound connections section select 'workshop-domain-follower' and click approve

# --------------
# Step 2
# --------------
leader_os_url = '<os_domain_endpoint_url>'
follower_os_url = '<os_domain_endpoint_url>'

os_cred = ('OSMasterUser', 'AwS#OpenSearch1')


def generate_insert():
  log_messages = ["Error out of memory", "High CPU!", "Things are normal", "I'm afraid I can't do that Dave."]
  return {
    "eventtime": datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S'),
    "ip-address": "8.8.8.8",
    "application-id": random.randint(1,9),
    "log-message": random.choice(log_messages)
  }

# Check if the index already exists. If so, just insert a new log record
create_index_r = requests.get(leader_os_url + '/log-data-1', auth=os_cred)
if (create_index_r.status_code != 404):
  ## just insert records
  print ("Index exists. Adding more data.")
  insert_document_r_body = generate_insert()
  print (insert_document_r_body)
  insert_document_r = requests.post(leader_os_url + '/log-data-1/_doc', auth=os_cred, headers= {'Content-type': 'application/json'}, data=json.dumps(insert_document_r_body))
  print(insert_document_r.text)

  ## get replication status
  print("\nReplication status:")
  repl_status = requests.get(follower_os_url + '/_plugins/_replication/log-data-1/_status', auth=os_cred)
  print(repl_status.text)

  exit(0)


# --------------
# Step 3
# --------------

# Create an index on leader os cluster, insert
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
        "format": "yyyy-MM-dd hh:mm:ss"
      },
      "ip-address": {
        "type": "text"
      },
      "application-id": {
        "type": "integer"
      },
      "log-message": {
        "type": "text"
      }
    }
  }
}

create_index_r = requests.put(leader_os_url + '/log-data-1', auth=os_cred, headers= {'Content-type': 'application/json'}, data=json.dumps(create_index_r_body))

print('------ Step 3 - Create an index on leader os cluster ------')
print(create_index_r.text)
print('------')

# --------------
# Step 4
# --------------

# Insert a document in an index log-data-1 (on leader os cluster)
insert_document_r_body = generate_insert()

insert_document_r = requests.put(leader_os_url + '/log-data-1/_doc/1', auth=os_cred, headers= {'Content-type': 'application/json'}, data=json.dumps(insert_document_r_body))

print('------ Step 4 - Insert a document in an index log-data-1 (on leader os cluster) ------')
print(insert_document_r.text)
print('------')

# --------------
# Step 5
# --------------

# Create a replication rule on the follower cluster to auto replicate all indices starting with log
create_replicate_r_body = {
   "leader_alias" : "workshop-domain-leader",
   "name": "log-data",
   "pattern": "log*",
   "use_roles":{
      "leader_cluster_role": "all_access",
      "follower_cluster_role": "all_access"
   }
}

create_replicate_r = requests.post(follower_os_url + '/_plugins/_replication/_autofollow', auth=os_cred, headers= {'Content-type': 'application/json'}, data=json.dumps(create_replicate_r_body))

print('------ Step 5 - Create a replication rule on the follower cluster to auto replicate all indices starting with log ------')
print(create_replicate_r.text)
print('------')

# --------------
# Step 5
# --------------

# Log into the follower cluster's dashboard and validate that you can see the replicated index
# Un: OSMasterUser
# Pw: AwS#OpenSearch1

#
# More information on opensearch cross cluster replication can be found HERE - https://docs.aws.amazon.com/opensearch-service/latest/developerguide/replication.html
#
