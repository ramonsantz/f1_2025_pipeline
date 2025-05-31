#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df_race = pd.read_csv("../data/raw/race_results_2025.csv")
df_fastest = pd.read_csv('../data/raw/fastest_laps_2025.csv')


# In[2]:


# (snack_case)
df_race.columns = df_race.columns.str.strip().str.lower().str.replace(' ','_')
df_fastest.columns = df_fastest.columns.str.strip().str.lower().str.replace(" ", '_')

# To numeric
df_race['starting_grid'] = pd.to_numeric(df_race['starting_grid'], errors='coerce')
# [positions] be float type for pilots who abandoned exist
df_race['position'] = pd.to_numeric(df_race['position'], errors='coerce') 

df_race.info()

# In[6]:


# Driver/track name cleanup
df_race['driver'] = df_race['driver'].str.strip().str.title()
df_race['track'] = df_race['track'].str.strip().str.title()

df_fastest['driver'] = df_fastest['driver'].str.strip().str.title()
df_fastest['grand_prix'] = df_fastest['grand_prix'].str.strip().str.title()

df_fastest.tail()

# In[4]:


# Auxiliary columns - racing efficiency (gaining positions)
df_race['position_gain'] = df_race['starting_grid'] - df_race['position']


# In[5]:


# Save the transformed data
df_race.to_csv('../data/processed/race_results_2025_clean.csv', index=False)
df_fastest.to_csv('../data/processed/fastest_laps_2025_clean.csv', index=False)
