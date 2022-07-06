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

# Define functions to be used later in the code ...
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

# --------------
# Step 1
# --------------
os_url = '<os_domain_endpoint_url>'

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

create_index_r = requests.put(os_url + '/log-data-1', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(create_index_r_body))

print('------ Create an index on os cluster ------')
print(create_index_r.text)
print('------')

# --------------
# Step 3
# --------------

print('------ Sending documents ------')

ip_address_array = ['52.95.4.6', '52.95.8.11', '52.95.6.2', '52.95.1.3', '52.95.14.13']
application_id_array = [1, 2, 3, 4, 5]
log_message_array = ['Error out of memory', 'Warning memory utilization above 80%', 'Warning CPU utilization above 80%', 'Warning CPU utilization above 50%', 'Warning remaining disk space 20%']

start = datetime.strptime('1/1/2020 12:00 AM', '%m/%d/%Y %I:%M %p')
end = datetime.today()

number_of_log_messages_to_send = 10000
counter = 0

while counter < number_of_log_messages_to_send:
    
    ip_id_index = random.randint(0,4)

    insert_document_r_body = {
        "eventtime": str(random_date(start, end).strftime('%Y-%m-%d %I:%M:%S')),
        "ip-address": ip_address_array[ip_id_index],
        "application-id": application_id_array[ip_id_index],
        "log-message": log_message_array[random.randint(0,4)]
    }
    
    insert_document_r = requests.put(os_url + '/log-data-1/_doc/' + str(counter+1), auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(insert_document_r_body))
    
    print('Message #' + str(counter+1) + ' | ' + insert_document_r.text)
    
    # print(json.dumps(insert_document_r_body))
    
    counter = counter + 1

print('------')
