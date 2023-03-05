# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 07:57:31 2023

@author: Ranjitha Dhanasekaran, PhD
@company: 3Cloud, LLC
"""
# Import Libraries
import os
from azureml.core import Workspace

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory
os.chdir('C:\AzureMachineLearning')

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Install Azure Machine Learning SDK for Python before running this code
# pip install azureml-sdk
# pip install azureml-core


# Create a workspace
ws = Workspace.create(name='mlw-ranjitha-from-spyder', 
                      subscription_id='efc5a0e2-7106-4a45-88f4-c9359bc36a6f',
                      resource_group='eydatabook_rg',
                      create_resource_group=True,
                      location='eastus')

# Deploying KeyVault with name mlwranjikeyvault2c924a4e.
# Deploying StorageAccount with name mlwranjistorage3e11f298b.
# Deployed KeyVault with name mlwranjikeyvault2c924a4e. Took 24.24 seconds.
# Deploying AppInsights with name mlwranjiinsights26d480db.
# Deployed AppInsights with name mlwranjiinsights26d480db. Took 70.23 seconds.
# Deploying Workspace with name mlw-ranjitha-from-spyder.
# Deployed Workspace with name mlw-ranjitha-from-spyder. Took 20.95 seconds.

# Connect to workspace
#1. Connecting to a workspace
ws = Workspace.get(name='mlw-ranjitha-from-spyder',
                   subscription_id='efc5a0e2-7106-4a45-88f4-c9359bc36a6f',
                   resource_group='eydatabook_rg')

ws.write_config(path=".", file_name="ws_config.json")

#2. Connect to a workspace using workspace configuration file downloaded from
# the Overview page of its blade in the Azure portal or from Azure Machine Learning studio. 

ws = Workspace.from_config()
ws.get_details()


