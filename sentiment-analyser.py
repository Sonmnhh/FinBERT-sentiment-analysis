#!/usr/bin/env python
# coding: utf-8



# In[19]:


import streamlit as st  
from textblob import TextBlob 


# In[20]:


st.title("Sentiment Analysis WebApp.")  
t = st.text_area("Please Enter your Sentences!") 


# In[27]:


if st.button("Analyze the Sentiment"):
    blob = TextBlob(message)
    result = blob.sentiment
    plrty = result.polarity
    subjty = result.subjectivity

    if plrty < 0:
        st.warning("The given text has negative sentiments associated with it: " + str(plrty))

    elif plrty > 0:
        st.success("The given text has positive sentiments associated with it: " + str(plrty))

    else:
        st.info("The given text has neutral sentiments associated with it: " + str(plrty))


    st.success(result)  


# In[ ]:




