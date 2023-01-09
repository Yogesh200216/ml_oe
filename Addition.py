#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
a = st.number_input("Enter first number")
b = st.number_input("Enter Second number")

result = a+b;
st.success("The result is {}".format(result))
print(result)


# In[ ]:




