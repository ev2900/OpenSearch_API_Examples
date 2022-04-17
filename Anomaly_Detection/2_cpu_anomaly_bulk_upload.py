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
os_url = 'https://search-workshop-domain-4oiko4q6pqxzslr3xdswkxsk6a.us-east-1.es.amazonaws.com'

# --------------
# Step 2
# --------------

print('------ Sending documents ------')

# Spike the CPU of application 2
start = datetime.today() - relativedelta(months=+36)
end = datetime.today()

number_of_anomaly_to_create = 90

document_id_start_position = 10000

application_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for application_id in application_ids:

    anomaly_counter = 0

    while anomaly_counter < number_of_anomaly_to_create:
    
        eventtime = str(random_date(start, end).strftime('%Y-%m-%d'))
    
        rel_start = eventtime + ' 12:00 AM'
        rel_start_object = datetime.strptime(rel_start, '%Y-%m-%d %I:%M %p')
        
        rel_end = eventtime + ' 12:00 PM'
        rel_end_object = datetime.strptime(rel_end, '%Y-%m-%d %I:%M %p')
    
        random_date(rel_start_object, rel_end_object)
        
        number_of_batchs_to_send = random.randint(1,3)
        
        current_number_of_batchs_sent = 0
        
        while current_number_of_batchs_sent < number_of_batchs_to_send:
            
            bulk_documents_r_body = ''
            bulk_insert_batch_size = 500
            current_bulk_insert_batch_size = 0
            
            while current_bulk_insert_batch_size < bulk_insert_batch_size:

                document_id_start_position = document_id_start_position + 1
            
                document = {
                  "eventtime": str(random_date(start, end).strftime('%Y-%m-%d %I:%M:%S')),
                  "application_id": 'Application ' + str(application_id),
                  "cpu_util": random.randint(85,100),
                  "memory_util": random.randint(1,25),
                  "disk_util": random.randint(1,25)
                }
          
                meta_data = {
                    "index": 
                    {
                        "_id": str(document_id_start_position)
                    }
                }
                
                bulk_documents_r_body = str(bulk_documents_r_body) + str(meta_data) + str('\n')
                bulk_documents_r_body = str(bulk_documents_r_body) + str(document) + str('\n')
        
                current_bulk_insert_batch_size = current_bulk_insert_batch_size + 1
            
            bulk_insert_response = requests.post(os_url + '/infa-logs-1/_bulk/', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/x-ndjson'}, data=bulk_documents_r_body.replace("'", "\""))
            print('Application # '+ str(application_id) + '/10 | Anomaly # ' + str(anomaly_counter) + '/' + str(number_of_anomaly_to_create) + ' | Batch # ' + str(current_number_of_batchs_sent) + '/' + str(number_of_batchs_to_send))
            
            current_number_of_batchs_sent = current_number_of_batchs_sent + 1
            
        anomaly_counter = anomaly_counter + 1