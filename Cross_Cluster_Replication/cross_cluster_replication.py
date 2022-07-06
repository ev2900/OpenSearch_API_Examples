# --------------
# Prerequisite
# --------------
# If you have not already installed the requests package and/or the json package 
# a. pip install requests
# b. pip install json

import requests
import json

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

create_index_r = requests.put(leader_os_url + '/log-data-1', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(create_index_r_body))

print('------ Step 3 - Create an index on leader os cluster ------')
print(create_index_r.text)
print('------')

# --------------
# Step 4
# --------------

# Insert a document in an index log-data-1 (on leader os cluster)
insert_document_r_body = {
  "eventtime": "2022-02-25 01:00:00",
  "ip-address":"52.95.4.6",
  "application-id": 1,
  "log-message":"Error out of memory"
}

insert_document_r = requests.put(leader_os_url + '/log-data-1/_doc/1', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(insert_document_r_body))

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

create_replicate_r = requests.post(follower_os_url + '/_plugins/_replication/_autofollow', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(create_replicate_r_body))

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
