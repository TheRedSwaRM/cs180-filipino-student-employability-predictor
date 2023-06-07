"""
The following acts as the main page of the web app.
For future additions, Streamlit identifies Markdown text.
"""

import streamlit as st

if 'Current Page' in st.session_state:
    st.session_state['Current Page'] = 0

st.set_page_config(initial_sidebar_state="collapsed")