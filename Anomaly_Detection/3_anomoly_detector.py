# --------------
# Prerequisite
# --------------
# If you have not already installed the requests package and/or the json package 
# a. pip install requests

import requests
import json

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
os_url = 'https://search-workshop-domain-atyey3n6ezpbugcxlk623l5ayi.us-east-1.es.amazonaws.com'

# --------------
# Step 2 - Create anomoly detector
# --------------
create_detector_body = {
  "name": "high-cpu",
  "description": "High CPU Anomaly Detector",
  "time_field": "eventtime",
  "indices": [
    "infa-logs*"
  ],
  "feature_attributes": [
    {
      "feature_name": "test",
      "feature_enabled": True,
      "aggregation_query": {
        "test": {
          "sum": {
            "field": "cpu_util"
          }
        }
      }
    }
  ],
  "detection_interval": {
    "period": {
      "interval": 1440,
      "unit": "Minutes"
    }
  },
  "window_delay": {
    "period": {
      "interval": 1,
      "unit": "Minutes"
    }
  },
  "category_field": [
    "application_id"
  ]
}

create_detector_r = requests.post(os_url + '/_plugins/_anomaly_detection/detectors', auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'}, data=json.dumps(create_detector_body))

print('------ Created an anomoly detector ------')
print(create_detector_r.text)
print('------')

# --------------
# Step 3 - Train anomoly detector
# --------------

# the code below does not work. I need to finish this

train_body = {
  "start_time": 1633048868000,
  "end_time": 1633394468000
}



POST _plugins/_anomaly_detection/detectors/AVDDBYABJkiJN-Gi3zx7/_start
{
  "start_time": 1633048868000,
  "end_time": 1633394468000
}
