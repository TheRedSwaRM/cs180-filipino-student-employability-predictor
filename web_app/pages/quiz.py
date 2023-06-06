"""
The following acts as the main page of the web app.
For future additions, Streamlit identifies Markdown text.
"""

# Initial configurations
import streamlit as st
import numpy as np
import pickle
st.set_page_config(initial_sidebar_state="collapsed")

# God didn't let me use enums. F*ck this sh*t.
# No. We can't set it as 0 outside. Else it breaks.
if 'Current Page' not in st.session_state:
    st.session_state['Current Page'] = 0

@st.cache_resource
def load_model():
    """Loads model globally to lessen downtime during reloads.

    Returns:
        _scikit_model_: A saved model from previous training tests.
    """
    return pickle.load(open("files/mlp_model.sav", 'rb'))

loaded_model = load_model()


def predict_answers(m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf):
    """Predicts the answers given 7 integer inputs, outputting a string that is either
    "Employable" or "LessEmployable"

    Args:
        m_app (int): The integer equivalent of a student's apperance.
        m_speak (int): The integer equivalent of a student's ability to speak.
        m_phys (int): The integer equivalent of a student's phyiscal health.
        m_mental (int): The integer equivalent of a student's mental health.
        m_conf (int): The integer equivalent of a student's confidence.
        m_ideas (int): The integer equivalent of a student's ability to create ideas.
        m_comm (int): The integer equivalent of a student's ability to communicate.
        m_perf (int): The integer equivalent of a student's performance.

    Returns:
        str: The string prediction from the model.
    """
    features = np.array([[m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf]])
    return loaded_model.predict(features)[0]

#============================
# Form
# Vaccaria: Lord forgive me for I will do something so vile, you will kill me for it.
# GENERAL APPEARANCE          = 0
# MANNER OF SPEAKING          = 1
# PHYSICAL CONDITION          = 2
# MENTAL ALERTNESS            = 3
# SELF CONFIDENCE             = 4
# ABILITY TO PRESENT_IDEAS    = 5
# COMMUNICATION SKILLS        = 6
# STUDENT PERFORMANCE RATING  = 7
#============================

def next():
    st.session_state['Current Page'] += 1
    
def prev():
    st.session_state['Current Page'] -= 1

def reset_quiz():
    st.session_state['Current Page'] = 0

# Debug
st.session_state

# GENERAL APPEARANCE
if st.session_state['Current Page'] == 0:
    st.write("GENERAL APPEARANCE")
    
    # item 1
    st.write("In a Formal Interview, what outfit do you see yourself wearing?")
    m_app_choice_1 = st.radio(label='Choices', options=["insert image here", "insert another image here"])
    # item 2
    st.write("In a Casual Interview (say, at a coffee shop), what outfit do you see yourself wearing?")
    m_app_choice_2 = st.radio(label='Choices', options=["insert other image here", "insert another image here"])

    # item 3
    st.write("In a Group Interview, what outfit do you see yourself wearing?")
    m_app_choice_3 = st.radio(label='Choices', options=["insert another image here", "insert another image here"])

    # m_app = st.slider('General Appearance', 1, 4) + 1           # Make it a 4-choice quiz section where the question assesses the person with how they present themselves in an interview
    # m_speak = st.slider('Manner of Speaking', 1, 4) + 1         # 4-choice items where they pick which dialogue option most describes them based on a prompt (can be a random prompt) 
    # m_phys = st.slider('Physical Condition', 1, 4) + 1          # Scale or self-assessment item (ask how physically fit do they see themselves as)
    # m_mental = st.slider('Mental Alertness', 1, 4) + 1          # Use this test as reference (src: https://www.jobtestprep.com/thurstone-test-mental-alertness)
    # m_conf = st.slider('Self-Confidence', 1, 4) + 1             # Self-assessment item
    # m_ideas = st.slider('Ability to Present Ideas', 1, 4) + 1   # See in brainstorming channel
    # m_comm = st.slider('Communication Skills', 1, 4) + 1        # Self-assessment of their: Tone of Voice, Posture, Body Language, Reading Comprehension, Level of Interest, Confidence, Honesty, Defensiveness (src: https://www.indeed.com/recruitment/c/info/assessing-communication-skills)
    # m_perf = st.slider('Student Performance Rating', 1, 4) + 1  # Can use a Standardized Assessment Test or just flat out ask them their GWA (like in ranges) (src: )

    next_button = st.button(label="Next",on_click=next)

# MANNER OF SPEAKING
elif st.session_state['Current Page'] == 1:
    st.write("MANNER OF SPEAKING")
    # item 1
    st.write("Scenario 1: {insert scenario here}, what would you say?")
    m_speak_choice_1 = st.radio(label='Choices', options=["insert choice here", "insert another choice here"])
    
    # item 2
    st.write("Scenario 2: {insert scenario here}, what would you say?")
    m_speak_choice_2 = st.radio(label='Choices', options=["insert a choice here", "insert another choice here"])
    
    # item 3
    st.write("Scenario 3: {insert scenario here}, what would you say?")
    m_speak_choice_3 = st.radio(label='Choices', options=["insert any choice here", "insert another choice here"])

    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)

    
# PHYSICAL CONDITION
elif st.session_state['Current Page'] == 2:
    st.write("PHYSICAL CONDITION")
    
    # item
    st.write("How physically fit do you see yourself?")
    m_phys = st.select_slider(label = "Slide to the appropriate", options=("haven't been active", "could improve myself", "doing okay", "well-rounded"))

    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)

    
# MENTAL ALERTNESS
elif st.session_state['Current Page'] == 3:
    st.write("MENTAL ALERTNESS")

    st.write("Jack and Jill have 44 cookies together. Jack has three times more cookies than Jill, how many cookies does he have?") # need to change this question
    m_mental = st.radio(Label="Choices", options=["yes", "no", "maybe", "so"])

    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)

    st.write("Questions based on https://www.jobtestprep.com/thurstone-test-mental-alertness")

    
# SELF CONFIDENCE
elif st.session_state['Current Page'] == 4:
    st.write("SELF CONFIDENCE")
    
    # item
    st.write("How confident do you see yourself?")
    m_phys = st.select_slider(label = "Slide to the prompt that best describes you", options=("I wish I am", "Somewhat", "Pretty much", "YEEEEEEEEEAAAAAAAAAAAH"))

    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)

    
# ABILITY TO PRESENT IDEAS
elif st.session_state['Current Page'] == 5:
    st.write("ABILITY TO PRESENT IDEAS")
    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)


# COMMUNICATION SKILLS
elif st.session_state['Current Page'] == 6:
    st.write("COMMUNICATION SKILLS")
    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)


# STUDENT PERFORMANCE RATING
elif st.session_state['Current Page'] == 7:
    st.write("STUDENT PERFORMANCE RATING")
    back_button = st.button(label="Back",on_click=prev)
    submit_button = st.button(label="Submit", on_click=next)

elif st.session_state['Current Page'] == 8:
    st.write("YOUR RESULTS:")
    # predict here
    # results = predict_answers(m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf)
    # "pretend" to load here
    # if-else statement showing the appropriate response wherein if employable, say something like "Congratulations! Looks like you have what it takes to get a job! Omi job!"
    pass