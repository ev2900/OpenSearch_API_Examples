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

# --------------
# Step 1 - Update this URL with your domain endpoint
# --------------
os_url = 'https://search-workshop-domain-t67jt2mhmfhfv7mo3obcbczw4a.us-east-1.es.amazonaws.com'

# --------------
# Step 2
# --------------

# Produce a baseline of normal data for the last 6 months
number_of_log_messages_to_send = 1
counter = 0

while counter < number_of_log_messages_to_send:
    
    #"eventtime": str(datetime.today().strftime('%Y-%m-%d %I:%M:%S')),
    
    insert_document_r_body = {
        "eventtime": str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')),
        "application_id": 'Application ' + str(random.randint(1,10)),
        "cpu_util": random.randint(85,100),
        "memory_util": random.randint(1,25),
        "disk_util": random.randint(1,25)
    }
    
    insert_document_r = requests.put(os_url + '/alert-1/_doc/3', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(insert_document_r_body))
    
    print('Message #' + str(counter+1) + ' | ' + str(insert_document_r_body) + ' | ' + insert_document_r.text)
    
    # print(json.dumps(insert_document_r_body))
    
    counter = counter + 1

print('------')