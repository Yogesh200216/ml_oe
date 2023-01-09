#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import csv
a = st.number_input("Enter first number")
b = st.number_input("Enter Second number")

result = a+b;
st.success("The result is {}".format(result))
print(result)
filename = "Addition_result.csv"

with open(filename, 'w') as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writeroe(result)

# In[ ]:




