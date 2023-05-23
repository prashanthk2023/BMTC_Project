#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_parquet('BMTC.parquet.gzip', engine='pyarrow')

input_df=pd.read_csv('input.csv')

# duplicated gives a boolean array for datapoints in rows with similar values

duplicate_mask=df.duplicated(subset=['BusID','Timestamp'],keep=False)

duplicate_df=df[duplicate_mask]

groups=duplicate_df.groupby(['BusID','Timestamp'])

rows_to_remove = []

for group_name, group_data in groups:
    if len(group_data['Latitude'].unique()) > 1 or len(group_data['Longitude'].unique()) > 1:
        rows_to_remove.extend(group_data.index.tolist())
        
df_cleaned = df.drop(rows_to_remove)

