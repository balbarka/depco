# Folder Structure

The project folder structure should be a convention followed by members of the development team. Provided below are the the folder location conventions used in this project. These are not considered the definative location that folder must be, but reviewing them will provide a reference for your consideration:
 - python: the python folder is provided to include the actual code that will be packages. It will inculde the setup.py file as well as include tests.
   - python/tests: placing the tests folder within python isn't necessary, but it keeps tests out of the root folder.
   - python/depco: while this will sometimes be seen as src or other indicator that the application code is in the folder, we've gone ahead here and names the application code folder the same as the package module name, depco.
 - deploy: This folder contains all files related the deployment pipeline. In this case, an azure devops deployment pipeline. The files included are:
   - azure-pipelines.yml: This is the actual pipline you should reference in azure devops. **NOTE**: This is currently written to trigger on any changes to the python folder when there are commits to main.
   - create-cluster.json - This is the cluster definition of the databricks unit test cluster. To keep things tidy, it is provided as a separate file instead of inline of the azure-pipeline.yml
   - environment.yml - We actually create a new conda environment during the pipeline for unit testing. This is the conda evironment definition.
   - wait_until_running.sh - This is a helper script to wait until the test cluster is running before we proceed with following stages. This is provided to keep the azure-pipelines.yml file tidy.
 - ref: folder to hold reference docs on the depco project.

**NOTE**: The directory for the project was provided with the azure devops pipeline to make it easier to understand the pipeline working directories. Be sure if other folder conventions are adopted to make the coresponding changes to your devops pipeline.
