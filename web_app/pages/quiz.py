"""
The following acts as the main page of the web app.
For future additions, Streamlit identifies Markdown text.
"""

# Initial configurations
import streamlit as st
import numpy as np
import pickle
st.set_page_config(initial_sidebar_state="collapsed")

@st.cache_resource
def load_model():
    return pickle.load(open("files/mlp_model.sav", 'rb'))

loaded_model = load_model()

def predict_answers(m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf):
    features = np.array([[m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf]])
    return loaded_model.predict(features)[0]

with st.form("quiz_form"):   
    m_app = st.slider('General Appearance', 1, 4) + 1           # Make it a 4-choice quiz section where the question assesses the person with how they present themselves in an interview
    m_speak = st.slider('Manner of Speaking', 1, 4) + 1         # 4-choice items where they pick which dialogue option most describes them based on a prompt (can be a random prompt) 
    m_phys = st.slider('Physical Condition', 1, 4) + 1          # Scale or self-assessment item (ask how physically fit do they see themselves as)
    m_mental = st.slider('Mental Alertness', 1, 4) + 1          # Use this test as reference (src: https://www.jobtestprep.com/thurstone-test-mental-alertness)
    m_conf = st.slider('Self-Confidence', 1, 4) + 1             # Self-assessment item
    m_ideas = st.slider('Ability to Present Ideas', 1, 4) + 1   # See in brainstorming channel
    m_comm = st.slider('Communication Skills', 1, 4) + 1        # Self-assessment of their: Tone of Voice, Posture, Body Language, Reading Comprehension, Level of Interest, Confidence, Honesty, Defensiveness (src: https://www.indeed.com/recruitment/c/info/assessing-communication-skills)
    m_perf = st.slider('Student Performance Rating', 1, 4) + 1  # Can use a Standardized Assessment Test or just flat out ask them their GWA (like in ranges) (src: )

    if submitted := st.form_submit_button("Submit"):
        st.markdown("You are:")
        st.write(m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf)
        st.write(predict_answers(m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf))