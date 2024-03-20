import os
import json
import streamlit as st

try:
    session_id = os.environ.get('current_session')
except:
    session_id = None

try:
    session_status = json.loads(os.environ.get(session_id).lower())
except:
    session_status = None


data_path = f'{os.getcwd()}/data/{session_id}/'

if session_status:
    account_path = f'{data_path}/account/'
    with open(f'{account_path}/user.json', 'r') as json_file:
        user_data = json.load(json_file)
    st.image(f'{account_path}/avatar.png')
    st.write(f"Hello {user_data['username']}!")
