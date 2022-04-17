# --------------
# Prerequisite
# --------------
# If you have not already installed the requests package and/or the json package 
# a. pip install requests
# b. pip install json

import requests
import json
import random

from datetime import datetime
from random import randrange
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# Define functions to be used later in the code ...
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

# --------------
# Step 1 - Update this URL with your domain endpoint
# --------------
os_url = 'https://search-workshop-domain-4oiko4q6pqxzslr3xdswkxsk6a.us-east-1.es.amazonaws.com'

# --------------
# Step 2
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
        "format": "yyyy-MM-dd hh:mm:ss"
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

create_index_r = requests.put(os_url + '/infa-logs-1', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(create_index_r_body))

print('------ Created an index on os cluster ------')
print(create_index_r.text)
print('------')

# --------------
# Step 3
# --------------

print('------ Sending documents ------')

# Produce a baseline of normal data for the last 6 months
start = datetime.today() - relativedelta(months=+36)
end = datetime.today()

bulk_insert_batch_size = 500

number_of_batchs_to_send = 200
current_number_of_batchs_sent = 0

document_id = 0

while current_number_of_batchs_sent < number_of_batchs_to_send:

  bulk_documents_r_body = ''
  current_bulk_insert_batch_size = 0
  
  while current_bulk_insert_batch_size < bulk_insert_batch_size:
      
      document_id = document_id + 1
      
      document = {
          "eventtime": str(random_date(start, end).strftime('%Y-%m-%d %I:%M:%S')),
          "application_id": 'Application ' + str(random.randint(1,10)),
          "cpu_util": random.randint(1,25),
          "memory_util": random.randint(1,25),
          "disk_util": random.randint(1,25)
      }
      
      meta_data = {
        "index": 
          {
            "_id": str(document_id)
          }
        }
    
      bulk_documents_r_body = str(bulk_documents_r_body) + str(meta_data) + str('\n')
      bulk_documents_r_body = str(bulk_documents_r_body) + str(document) + str('\n')
    
      current_bulk_insert_batch_size = current_bulk_insert_batch_size + 1

  bulk_insert_response = requests.post(os_url + '/infa-logs-1/_bulk/', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/x-ndjson'}, data=bulk_documents_r_body.replace("'", "\""))
  
  #print(bulk_insert_response.text)
  print('Batch # ' + str(current_number_of_batchs_sent) + " sent")
  
  current_number_of_batchs_sent = current_number_of_batchs_sent + 1

print('------')