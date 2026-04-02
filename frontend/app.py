import streamlit as st
import requests

API = 'http://backend:8000/research'

st.title('Multi-Agent Research AI')

query = st.text_area('Ask a research question')

if st.button('Research'):
    with st.spinner('Researching...'):
        res = requests.post(API, json={'query': query})
        data = res.json()

    st.subheader('Research Output')
    st.write(data.get('final_answer'))