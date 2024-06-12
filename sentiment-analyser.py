#!/usr/bin/env python
# coding: utf-8



# In[19]:


import streamlit as st  
from textblob import TextBlob 
import pandas as pd

# In[20]:
# Sidebar navigation
st.sidebar.title("For Financial")
page = st.sidebar.radio("Go to", ["Home", "News", "Contact Me"])
        
# Add custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #333333;
        text-align: center;
        margin-bottom: 20px;
    }
    p {
        color: #666666;
        text-align: center;
        font-size: 18px;
    }
    input {
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .decorative {
        background-image: url('https://www.transparenttextures.com/patterns/white-waves.png');
        padding: 50px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Financial Sentiment Analysis WebApp.")  
st.write('Welcome to my sentiment analysis app!')
message = st.text_area('Enter your sentence here')


# In[27]:


if st.button("Analyze the Sentiment"):
    if message:
        blob = TextBlob(message)
        result = blob.sentiment
        plrty = result.polarity
        subjty = result.subjectivity
        sentiment = "Neutral"

    if plrty < 0:
        st.warning("The given text has negative sentiments associated with it: " + str(plrty))

    elif plrty > 0:
        st.success("The given text has positive sentiments associated with it: " + str(plrty))

    else:
        st.info("The given text has neutral sentiments associated with it: " + str(plrty))
        
        # Append result to the session state
        st.session_state.sentiment_results.append({"No.": len(st.session_state.sentiment_results) + 1, "Text": message, "Sentiment": sentiment})
        st.success(result)

# Display results table
if st.session_state.sentiment_results:
    st.subheader("Analyzed Sentiments")
    results_df = pd.DataFrame(st.session_state.sentiment_results)
    st.table(results_df)

# In[28]:




