# DepCo Reference CICD

DepCo is a fictitious company that is deploying an application on Azure Databricks. Since there can be an overwhelming number of options when devloping, this is intended to provide referential code on how to deploy with the following pre-supposed decisions:
 - Using Databricks Runtime LTS ML 7.3
 - Deploying an application as a python wheel file
 - Development will be done in a local conda environment with a matching python verion to the Databricks Runtime ML 7.3
 - Authentication via PAT
 - leverage azure devops repo and pipeline
 - ensure that code deployed has both test and coverage reports in azure
 - deployment will be directly to a databricks cluster
