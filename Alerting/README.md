# Alerting

Follow the instructions below

1. Run the CloudFormation stack below. It will create the required resources required for this example

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=os-alerting&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_demo_alerting.yaml)

The resources created by the CloudFormation stack are documented in the architecture below

<img width="600" alt="Fluentd_cloud9_Architecture" src="https://github.com/ev2900/CloudFormation_Examples/blob/main/Architecture%20Diagrams%20for%20README/OpenSearch_demo_alerting_yaml.png">

2. Open the Cloud9 environment and create an index by running the [1_create_index.py](https://github.com/ev2900/OpenSearch_API_Examples/blob/main/Alerting/1_create_index.py) python script in the Cloud9 terminal

* Update the ```os_url``` variable with the URL of the OpenSearch domain endpoint

*Note the CloudFormation stack output section can provide you with the domain endpoint URL*

Once you have updated the values save the file and ```python 1_create_index.py``` in the Cloud9 terminal

3. Log into the OpenSearch dashboard (URL, UserName and Password can be found in the CloudFormation Stack Outputs) to set up a SNS alerting destination. On alerting OpenSearch plugin page add a destination and configure it as follows
   * Name = ```SNS Destination```
   * Type = ```Amazon SNS```    
   * SNS topic ARN = the TopicARN value from CloudFormation Stack output  
   * IAM role ARN = the IAMRoleARN value from CloudFormation Stack output

4. Set up a Monitor - an Alert. On alerting OpenSearch plugin page add a monitors and configure it as follows
  * Monitor name = ```High CPU Alert```
  * Monitor type = ```Per query monitor```
  * Monitor defining method = ```Visual editor```
  * Frequency = ```By interval```
  * Run every = ``` 1 ``` ```minute```
  * Index = ```alert-1```
  * Time field = ```eventtime```
  * Metric = ```MAX OF cpu_util```
  * Trigger
    * Trigger name = ```CPU over 50```
    * Severity level = ```1 (Highest)```
    * Trigger condition = ```IS ABOVE``` ```50```
  * Actions
    * Action name = ```Email Alert```
    * Destination = ```SNS Destination - (Amazon SNS)```
    * Message subject = ```High CPU!```
  
5. Open the Cloud9 environment and send sample data that will trigger an alert [2_trigger_alert.py](https://github.com/ev2900/OpenSearch_API_Examples/blob/main/Alerting/2_trigger_alert.py) python script in the Cloud9 terminal  

* Update the ```os_url``` variable with the URL of the OpenSearch domain endpoint

*Note the CloudFormation stack output section can provide you with the domain endpoint URL*

Once you have updated the values save the file and ```2_trigger_alert.py``` in the Cloud9 terminal
