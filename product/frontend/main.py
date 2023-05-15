import streamlit as st
import requests
url="http://app:8000/api/states"
def get_states():
    try:
        response=requests.get(url)
        return response.json()['states']
    except:
        return None


st.header("List of states")
st.table(get_states())
