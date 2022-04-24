# --------------
# Prerequisite
# --------------
# If you have not already installed the requests package and/or the json package 
# a. pip install requests
# b. pip install json

import requests
import json

# --------------
# Step 1 - Update this URL with your domain endpoint
# --------------
os_url = 'https://search-workshop-domain-t67jt2mhmfhfv7mo3obcbczw4a.us-east-1.es.amazonaws.com'

# --------------
# Step 2 - Create destination
# --------------


# --------------
# Step 3 - Create monitors
# --------------
POST _plugins/_alerting/monitors
{
  "type": "monitor",
  "name": "high_cpu_2",
  "monitor_type": "query_level_monitor",
  "enabled": true,
  "schedule": {
    "period": {
      "interval": 1,
      "unit": "MINUTES"
    }
  },
  "inputs": [{
    "search": {
      "indices": ["alert-1"],
      "query": {
        "size": 0,
        "aggregations": {},
        "query": {
          "bool": {
            "filter": {
              "range": {
                "@timestamp": {
                  "gte": "||-1h",
                  "lte": "",
                  "format": "epoch_millis"
                }
              }
            }
          }
        }
      }
    }
  }],
  "triggers": [{
    "name": "test-trigger",
    "severity": "1",
    "condition": {
      "script": {
        "source": "ctx.results[0].hits.total.value > 0",
        "lang": "painless"
      }
    },
    "actions": [{
      "name": "test-action",
      "destination_id": "ld7912sBlQ5JUWWFThoW",
      "message_template": {
        "source": "This is my message body."
      },
      "throttle_enabled": true,
      "throttle": {
        "value": 27,
        "unit": "MINUTES"
      },
      "subject_template": {
        "source": "TheSubject"
      }
    }]
  }]
}