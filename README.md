# OpenSearch API Examples

<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-3639-blue"> <img width="85" alt="map-user" src="https://img.shields.io/badge/views-1303-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-321-green">

Example Python programs that use the OpenSearch APIs for common tasks

---

The CloudFormation stack below launches a Cloud9 enviorment with this repository automaticlly cloned to it + an OpenSearch cluster.

This configuration works well for running the [Sample_Log_Data/](https://github.com/ev2900/OpenSearch_API_Examples/tree/main/Sample_Log_Data)

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=open-search-demo-cloud9-simple&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_demo_Cloud9_simple.yaml)

<img width="450" alt="KDA_studio_kinesis_demo_yaml" src="https://github.com/ev2900/CloudFormation_Examples/blob/main/Architecture%20Diagrams%20for%20README/OpenSearch_demo_Cloud9_simple_yaml.png">

---

The CloudFormation stack below launches a Cloud9 enviorment with this repository automaticlly cloned to it + two OpenSearch cluster that can be configured to replicate data from one cluster to another

This configuration works well for running the [Cross_Cluster_Replication/](https://github.com/ev2900/OpenSearch_API_Examples/tree/main/Cross_Cluster_Replication)

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=open-search-cross-cluster-replication&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_cross_cluster_replication_demo.yaml)

<img width="700" alt="OpenSearch_demo_VPC_Architecture" src="https://github.com/ev2900/CloudFormation_Examples/blob/main/Architecture%20Diagrams%20for%20README/OpenSearch_cross_cluster_replication_demo_yaml.png">

---

The CloudFormation stack below launches a Cloud9 enviorment with this repository automaticlly cloned to it + an OpenSearch cluster that can be configured to run an anomaly detection example

This configuration works well for running the [Anomaly_Detection/](https://github.com/ev2900/OpenSearch_API_Examples/tree/main/Anomaly_Detection)

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=os-anomaly-detection&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_demo_anomaly_detection.yaml)

<img width="450" alt="OpenSearch_demo_anomaly_detection_Architecture" src="https://github.com/ev2900/CloudFormation_Examples/blob/main/Architecture%20Diagrams%20for%20README/OpenSearch_demo_anomaly_detection_yml.png">

---

The CloudFormation stack below launches a Cloud9 enviorment with this repository automaticlly cloned to it + an OpenSearch cluster that can be configured to run the alerting example

This configuration works well for running the [Alerting/](https://github.com/ev2900/OpenSearch_API_Examples/tree/main/Alerting)

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=os-alerting&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_demo_alerting.yaml)

<img width="600" alt="Fluentd_cloud9_Architecture" src="https://github.com/ev2900/CloudFormation_Examples/blob/main/Architecture%20Diagrams%20for%20README/OpenSearch_demo_alerting_yaml.png">
