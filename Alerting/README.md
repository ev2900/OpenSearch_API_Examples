# Alerting

Follow the instructions below

1. Run the CloudFormation stack below. It will create the required resources required for this example

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=os-alerting&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_demo_alerting.yaml)

The resources created by the CloudFormation stack are documented in the architecture below

<img width="600" alt="Fluentd_cloud9_Architecture" src="https://github.com/ev2900/CloudFormation_Examples/blob/main/Architecture%20Diagrams%20for%20README/OpenSearch_demo_alerting_yaml.png">

2. Log into the OpenSearch dashboard 
* Navigate to the CloudFormation stack output section
* Open the DashboardURL and log in with the UserName and Password

3. Set up a SNS alerting destination in OpenSearch
* Using the left hand menu navigate to the alerting under the OpenSearch Plugins section
* On the alerting page navigate to the destinations section, Click on **Add destination**
* On the add destination page configure the destination as follows
   * Name ```SNS Destination```
   * Type ```Amazon SNS```    
   * SNS topic ARN = the TopicARN value from CloudFormation Stack output  
   * IAM role ARN = the IAMRoleARN value from CloudFormation Stack output
