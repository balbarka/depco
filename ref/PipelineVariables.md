# Pipeline Variables

Throughout the azure-pipelines.yml, there are refrences to variables that are set within azure devops.
Here are the descriptions of those variables which will need to be created in the azure devops pipeline UI:

| variable | description |
| -------- | ----------- |
| `WORKSPACE_HOST` | The hostname used to configure databricks-connect and databricks-cli. |
| `WORKSPACE_TOKEN` | The token used to configure databricks-connect and databricks-cli |
| `WORKSPACE_ORG` | The org used to configure databricks-connect. | 
| `TARGET_CLUSTER_ID` | The cluster id of where the package is deployed. **NOTE**: In production pipelines, you will typically deploy to a library repo, not directly to a target cluster. |
| `TEMP_CLUSTER_ID` | This is the only variable that actually isn't set ahead of time in the devops UI. Instead, this variable is generated in the *Create Databricks Test Cluster* step. |
| 
