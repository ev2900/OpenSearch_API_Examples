# --------------
# Prerequisite
# --------------
# If you have not already installed the requests package and/or the json package 
# a. pip install requests
# b. pip install json

import requests
import json
import random
import time

from datetime import datetime

# --------------
# Step 1 - Update this URL with your domain endpoint
# --------------
os_url = 'https://search-workshop-domain-4o7rkivj7fys3hzg6sowxsrmqq.us-east-1.es.amazonaws.com'

# --------------
# Step 2
# --------------

number_of_log_messages_to_send = 10
counter = 0
document_index_start = 0

while counter < number_of_log_messages_to_send:
    
    insert_document_r_body = {
        "eventtime": str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')),
        "application_id": 'Application ' + str(random.randint(1,10)),
        "cpu_util": random.randint(85,100),
        "memory_util": random.randint(1,25),
        "disk_util": random.randint(1,25)
    }
    
    insert_document_r = requests.put(os_url + '/alert-1/_doc/' + str(document_index_start), auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(insert_document_r_body))
    
    print('Message #' + str(counter + 1) + ' | ' + str(insert_document_r_body) + ' | ' + insert_document_r.text)

        
    counter = counter + 1
    document_index_start = document_index_start + 1
    
    time.sleep(30)
