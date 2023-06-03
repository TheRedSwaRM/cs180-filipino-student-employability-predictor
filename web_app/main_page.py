"""
The following acts as the main page of the web app.
For future additions, Streamlit identifies Markdown text.
"""

import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.title("Ready to take the next step? :student:")
st.markdown("Take the quiz to see if you're ready to take a job in the future!")

st.markdown('<a href="/quiz" target="_self">Next page</a>', unsafe_allow_html=True)