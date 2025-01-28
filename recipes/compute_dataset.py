# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Uncomment to use create_target() function from project library
#from myfunctions import create_target

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
customers_data_all_joined = dataiku.Dataset("customers_data_all_joined")
df = customers_data_all_joined.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Click on Variables, then Validate and click to place "revenue_value" in this code
# Then cast it to int and assign it the the variable "var"
var = int(dataiku.get_custom_variables()["revenue_value"])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Define function to compute target column
def create_target(row, v):
    revenue = row['revenue']
    if revenue >= v:
        target = 1
    elif revenue < v:
        target = 0
    else:
        target = revenue
    return target

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Call the create_target function to create target column
df['target'] = df.apply(create_target, axis = 1, v = var)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Print df for inspection
#df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
dataset = dataiku.Dataset("dataset")
dataset.write_with_schema(df)