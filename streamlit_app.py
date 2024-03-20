import os
import streamlit as st
from datetime import datetime

from scripts.utils import (
    create_hash_key,
    create_directory,
    unzip_bytes_data
)

# data path
data_path = f"{os.getcwd()}/data/"
create_directory(data_path)

# creating unique hash key
current_time = str(datetime.now())
hash_key = create_hash_key(current_time)

# ---- STREAMLIT LAYOUT CONFIGURATION ----
st.set_page_config(
    page_title="Discord Package Explorer", page_icon=":bar_chart:", layout="wide"
)

st.title("Discord Package Explorer")

# ---- SIDEBAR OPTIONS ----
with st.sidebar:
    uploaded_file = st.file_uploader(
        label="**Upload ZIP File**", accept_multiple_files=False, type=['.zip']
    )

    process_btn = st.button("Process")

    # If file is uploaded and button is pressed
    if (uploaded_file is not None) and process_btn:
        zip_data = uploaded_file.getvalue()
        extracted_path = f'{data_path}/{hash_key}/'
        create_directory(extracted_path)
        unzip_bytes_data(zip_data, extracted_path)
        st.success("Extraction successful.")
