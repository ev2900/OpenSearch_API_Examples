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
# Step 1 - - Update this URL with your domain endpoint
# --------------
os_url = 'https://search-workshop-domain-atyey3n6ezpbugcxlk623l5ayi.us-east-1.es.amazonaws.com'

# --------------
# Step 2
# --------------

print('------ Start ------')

# Spike the CPU of application 2
start = datetime.today() - relativedelta(months=+36)
end = datetime.today()

number_of_anomaly_to_create = 90
anomaly_counter = 0

index_counter = 10000

application_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for application_id in application_ids:

    while anomaly_counter < number_of_anomaly_to_create:
    
        eventtime = str(random_date(start, end).strftime('%Y-%m-%d'))
    
        rel_start = eventtime + ' 12:00 AM'
        rel_start_object = datetime.strptime(rel_start, '%Y-%m-%d %I:%M %p')
        
        rel_end = eventtime + ' 12:00 PM'
        rel_end_object = datetime.strptime(rel_end, '%Y-%m-%d %I:%M %p')
    
        print('------ Anomaly ' +  str(anomaly_counter) + ' | Start @ ' + str(rel_start) + ' | End @ ' + str(rel_end) + ' ------')
        
        random_date(rel_start_object, rel_end_object)
        
        number_of_log_messages_to_send = random.randint(500,1000)
        message_counter = 0
        
        print('------ Document Id Start @ ' + str(index_counter) + '------')
    
        while message_counter < number_of_log_messages_to_send:
        
            insert_document_r_body = {
                "eventtime": str(random_date(rel_start_object, rel_end_object).strftime('%Y-%m-%d %I:%M:%S')),
                "application_id": 'Application ' + str(application_id),
                "cpu_util": random.randint(85,100),
                "memory_util": random.randint(1,25),
                "disk_util": random.randint(1,25)
            }
        
            insert_document_r = requests.put(os_url + '/infa-logs-1/_doc/' + str(index_counter+1), auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(insert_document_r_body))
        
            print('Message #' + str(message_counter+1) + ' | ' + str(insert_document_r_body) + ' | ' + insert_document_r.text)
            
            # print('Message #' + str(message_counter+1) + ' | ' + str(insert_document_r_body))
            # print(json.dumps(insert_document_r_body))
        
            message_counter = message_counter + 1
            index_counter = index_counter + 1
            
            # print(index_counter)
    
        print('------ Anomaly ' +  str(anomaly_counter) + ' | Start @ ' + str(rel_start) + ' | End @ ' + str(rel_end) + ' ------')
        print('------ Document Id End @ ' + str(index_counter) + ' ------')
        print('------ Done ------')
        print(' ')
        
        anomaly_counter = anomaly_counter + 1