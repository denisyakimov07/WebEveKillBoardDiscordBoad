import requests
import streamlit as st

from bd import authentication


if st.experimental_get_query_params() and authentication(st.experimental_get_query_params()):
    server_id = st.experimental_get_query_params()['s'][0]
    print(st.experimental_get_query_params())
    r = requests.get(f"http://172.100.0.100:5000/server_text_channels/{server_id}").text
    st.text(r)
