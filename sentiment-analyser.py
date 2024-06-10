#!/usr/bin/env python
# coding: utf-8



# In[19]:


import streamlit as st  
from textblob import TextBlob 


# In[20]:


st.title("Sentiment Analysis WebApp.")  
st.write('Welcome to my sentiment analysis app!')
message = st.text_area('Enter your sentence here')


# In[27]:


if st.button("Analyze the Sentiment"):
    if message:
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




