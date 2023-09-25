import requests
import streamlit as st

from bd import authentication
from environment import get_env

if st.experimental_get_query_params() and authentication(st.experimental_get_query_params()):
    server_id = st.experimental_get_query_params()['s'][0]
    # headers = {'Authorization': f'Bearer {get_env().DISCORD_BOT_TOKEN}'}
    _json = {"username_key": get_env().HTTP_USERNAME, 'password_key': get_env().HTTP_PASSWORD}
    r = requests.get(f"http://172.100.0.101:80/server_text_channels/{server_id}", json=_json).text
    st.text(r)




grid = st.columns(4)

def add_row(row):
    with grid[0]:
        st.text_input('Expense', key=f'input_expense{row}')
        st.selectbox('Expense',options=['2', "3"])
    with grid[1]:
        st.number_input('Amount', key=f'input_amount{row}')
    with grid[2]:
        st.number_input('Budget', key=f'input_budget{row}')
    with grid[3]:
        st.number_input('Variance', key=f'input_variance{row}',
                        value = st.session_state[f'input_budget{row}'] \
                               -st.session_state[f'input_amount{row}'],
                        disabled=True)

for r in range(4):
    add_row(r)