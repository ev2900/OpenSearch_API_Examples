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
os_url = 'https://search-workshop-domain-rasyvcadldo6spty6dwhtsaw6y.us-east-1.es.amazonaws.com'


# --------------
# Step 2
# --------------

print('------ Sending documents ------')

# Spike the CPU of application 2
start = datetime.strptime('03/04/2022 12:00 AM', '%m/%d/%Y %I:%M %p')
end = datetime.today().strftime('%m/%d/%Y %I:%M %p')

number_of_log_messages_to_send = 200
counter = 0

while counter < number_of_log_messages_to_send:
    
    insert_document_r_body = {
        "eventtime": str(random_date(start, end).strftime('%Y-%m-%d %I:%M:%S')),
        "application_id": 2,
        "cpu_util": random.randint(85,100),
        "memory_util": random.randint(1,25),
        "disk_util": random.randint(1,25)
    }
    
    insert_document_r = requests.put(os_url + '/infa-logs-1/_doc/' + str(counter+1), auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(insert_document_r_body))
    
    print('Message #' + str(counter+1) + ' | ' + insert_document_r.text)
    
    # print(json.dumps(insert_document_r_body))
    
    counter = counter + 1

print('------')