# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:48:55 2023

@author: Ranjitha Dhanasekaran, PhD
@company: 3Cloud, LLC
"""
# Import Libraries
import os
from azureml.core import Workspace

ws = Workspace.from_config()
# Working with the Workspace Class
## Retrieve a dictionary object containing the compute targets defined in the workspace
for compute_name in ws.compute_targets:
    compute = ws.compute_targets[compute_name]
    print(compute.name, ":", compute.type)
    
# Handle to the workspace
from azure.ai.ml import MLClient

# Authentication package
from azure.identity import DefaultAzureCredential
from azure.identity import InteractiveBrowserCredential

#credential = DefaultAzureCredential()

credential = InteractiveBrowserCredential()

# Get a handle to the workspace
ml_client = MLClient(
    credential=credential,
    subscription_id='efc5a0e2-7106-4a45-88f4-c9359bc36a6f',  
    resource_group_name='eydatabook_rg',
    workspace_name='mlw-ranjitha-from-spyder',
)

# Create compute target
from azure.ai.ml.entities import AmlCompute

# Name assigned to the compute cluster
cpu_compute_target = "ci-aml-ranjitha1"

try:
    # check if the compute target already exists
    cpu_cluster = ml_client.compute.get(cpu_compute_target)
    print(
        f"Compute {cpu_compute_target} already exists. The compute size is {cpu_cluster.size}."
    )

except Exception:
    print("Creating a new compute...")

    # Create the Azure ML compute object with the intended parameters
    cpu_cluster = AmlCompute(
        name=cpu_compute_target,
        type="amlcompute",
        size="STANDARD_E4AS_V4",
        min_instances=0,
        max_instances=4,
        idle_time_before_scale_down=180,
        tier="Dedicated",
    )

    cpu_cluster = ml_client.compute.begin_create_or_update(cpu_cluster)

    print(
        f"Compute {cpu_cluster.name} was created. The compute size is {cpu_cluster.size}"
    )