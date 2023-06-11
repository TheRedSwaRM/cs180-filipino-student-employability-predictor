"""
The following acts as the main page of the web app.
For future additions, Streamlit identifies Markdown text.

To whoever's going to document this, someone read PEP.
Thanks. -Omi

"""

# Initial configurations
import streamlit as st
import numpy as np
import pickle
import math
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(initial_sidebar_state="collapsed")

# God didn't let me use enums. F*ck this sh*t.
# No. We can't set it as 0 outside. Else it breaks.
if 'Current Page' not in st.session_state:
    st.session_state['Current Page'] = 0

# To pretty much allow variables to be tracked in
# debug and also to allow it to change on the fly.
if 'Scores' not in st.session_state:
    st.session_state['Scores'] = [
        0,  #m_app
        0,  #m_speak
        0,  #m_phys
        0,  #m_mental
        0,  #m_conf
        0,  #m_ideas
        0,  #m_comm
        0   #m_perf
    ]

#TO DO: Initialize global variables here (?)

# m_app = 3
# m_speak = 3
# m_phys = 3
# m_mental = 3
# m_conf = 3
# m_ideas = 3
# m_comm = 3
# m_perf = 3

@st.cache_resource
def load_model():
    """Loads model globally to lessen downtime during reloads.

    Returns:
        _scikit_model_: A saved model from previous training tests.
    """
    return pickle.load(open('./files/mlp_model.sav', 'rb'))

@st.cache_resource
def load_scaler():
    """Loads model globally to lessen downtime during reloads.

    Returns:
        _scikit_model_: A saved model from previous training tests.
    """
    return pickle.load(open('./files/best_scaler.sav', 'rb'))


loaded_model = load_model()
loaded_scaler = load_scaler()



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
    # Fits input data into a 2D Array
    features = np.array([[m_app, m_speak, m_phys, m_mental, m_conf, m_ideas, m_comm, m_perf]])
    
    # Normalizes input
    features = loaded_scaler.transform(features)
    
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
    st.session_state['Scores'] = [
        0,  #m_app
        0,  #m_speak
        0,  #m_phys
        0,  #m_mental
        0,  #m_conf
        0,  #m_ideas
        0,  #m_comm
        0   #m_perf
    ]
    #Also reset global variables methinks

# Debug
# st.session_state

# GENERAL APPEARANCE - 0
if st.session_state['Current Page'] == 0:
    # st.write("GENERAL APPEARANCE")
    
    st.info("For clothing references, please see the images on the right")
    app_col1, app_col2, app_col3 = st.columns([0.40, 0.3,0.3])

    with app_col1:
        # item 1
        st.write("What outfit do you see yourself wearing in:")
        m_app_choice_1 = st.radio(
            label="A Formal Interview, where the company's employees usually wear semi-formal attire",
            options=["Semi-Formal Wear", "Business Casual Wear", "Formal Wear"]) # Best answers (from best to worst): Formal Wear, Semi-Formal Wear, Business Casual
    
        # item 2
        m_app_choice_2 = st.radio(
            label='In a Casual Interview at a coffee shop, knowing that your interviewer will wear something Smart Casual',
            options=["Business Casual Wear", "Casual Wear", "Formal Wear"]) # Best to Worst Answers: Business Casual Wear, Casual Wear, Formal Wear

        # item 3
        m_app_choice_3 = st.radio(
            label="In a Group Interview, where the company's dress code is casual",
            options=["Casual Wear", "Semi-Formal Wear", "Business Casual Wear"]) # Best to Worst Answers: Business Casual Wear, Semi-Formal Wear, Casual Wear

    with app_col2:
        img1 = st.image("files/formal_clothing.png", width = 200, caption="Formal Wear")
        img2 = st.image("files/semiformal_clothing.png", width = 200, caption="Semi-Formal Wear")

    with app_col3:
        img3 = st.image("files/businesscasual_clothing.png", width = 200, caption="Business Casual Wear")
        img4 = st.image("files/casual_clothing.png", width = 200, caption="Casual Wear")

    # God abandoned me this way.
    st.session_state['Scores'][0] = 0
    # First Answer
    if m_app_choice_1 == "Semi-Formal Wear":
        st.session_state['Scores'][0] += 4
    elif m_app_choice_1 == "Business Casual Wear":
        st.session_state['Scores'][0] += 3
    elif m_app_choice_1 == "Formal Wear":
        st.session_state['Scores'][0] += 5
    # Second Answer
    if m_app_choice_2 == "Formal Wear":
        st.session_state['Scores'][0] += 4
    elif m_app_choice_2 == "Business Casual Wear":
        st.session_state['Scores'][0] += 5
    elif m_app_choice_2 == "Casual Wear":
        st.session_state['Scores'][0] += 3
    # Third Answer
    if m_app_choice_3 == "Semi-Formal Wear":
        st.session_state['Scores'][0] += 4
    elif m_app_choice_3 == "Business Casual Wear":
        st.session_state['Scores'][0] += 5
    elif m_app_choice_3 == "Casual Wear":
        st.session_state['Scores'][0] += 3
    # Average the answers
    st.session_state['Scores'][0] = math.ceil(st.session_state['Scores'][0] / 3)
    
    next_button = st.button(label="Next",on_click=next)
    
    # TO DO: insert credits for images used here  

# MANNER OF SPEAKING - 1
elif st.session_state['Current Page'] == 1:
    # st.write("MANNER OF SPEAKING")
    # item 1
    m_speak_choice_1 = st.radio(
        label="You are addressing a customer complaint as a customer service representative, choose the most appropriate response",
        options=[
            "Sorry for the inconvenience caused. We'll do our best to resolve the issue shortly.",
            "It's not our fault. You should have read the terms and conditions more carefully.",
            "That's not my department. You need to speak with someone else."
            ]) # best to worst (by index): 0, 1, 2
    
    # item 2
    m_speak_choice_2 = st.radio(
        label='You are in a group discussion, and a team member continuously interrupts and dominates the conversation. How would you respond?',
        options=[
            "Say: Excuse me, but you're talking too much. Let others have a chance to speak.",
            "Say: I appreciate your enthusiasm, but it would be beneficial to hear other perspectives as well.",
            "(Let them continue what they're saying)"
            ]) # best to worst (by index): 1, 0, 2
    
    # item 3
    m_speak_choice_3 = st.radio(
        label='You are in a team meeting and a colleague presents an idea that you strongly disagree with. What would you say?',
        options=[
            "I think that idea won't work because...",
            "I appreciate your perspective, although I have different viewpoint on this because...",
            "I think your idea is completely off-track, the project's goal is to..."
            ]) # best to worst (by index): 1, 0, 2

    # God abandoned me this way.
    st.session_state['Scores'][1] = 0
    # First Answer
    if m_speak_choice_1 == "Sorry for the inconvenience caused. We'll do our best to resolve the issue shortly.":
        st.session_state['Scores'][1] += 5
    elif m_speak_choice_1 == "It's not our fault. You should have read the terms and conditions more carefully.":
        st.session_state['Scores'][1] += 4
    elif m_speak_choice_1 == "That's not my department. You need to speak with someone else.":
        st.session_state['Scores'][1] += 3
    # Second Answer
    if m_speak_choice_2 == "Say: Excuse me, but you're talking too much. Let others have a chance to speak.":
        st.session_state['Scores'][1] += 4
    elif m_speak_choice_2 == "Say: I appreciate your enthusiasm, but it would be beneficial to hear other perspectives as well.":
        st.session_state['Scores'][1] += 5
    elif m_speak_choice_2 == "(Let them continue what they're saying)":
        st.session_state['Scores'][1] += 3
    # Third Answer
    if m_speak_choice_3 == "I think that idea won't work because...":
        st.session_state['Scores'][1] += 4
    elif m_speak_choice_3 == "I appreciate your perspective, although I have different viewpoint on this because...":
        st.session_state['Scores'][1] += 5
    elif m_speak_choice_3 == "I think your idea is completely off-track, the project's goal is to...":
        st.session_state['Scores'][1] += 3
    # Average the answers
    st.session_state['Scores'][1] = math.ceil(st.session_state['Scores'][1] / 3)

    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)

# PHYSICAL CONDITION - 2
elif st.session_state['Current Page'] == 2:
    # st.write("PHYSICAL CONDITION")
    
    # item
    st.write("How physically fit do you see yourself?")
    m_phys = st.select_slider(
        label = "Slide to the appropriate", 
        options = (
            "not active much", 
            "I could improve myself", 
            "pretty okay", 
            "fit!"
            )
        )
    # God abandoned me this way.
    st.session_state['Scores'][2] = 0
    if m_phys == "not active much":
        st.session_state['Scores'][2] = 2
    elif m_phys == "I could improve myself":
        st.session_state['Scores'][2] = 3
    elif m_phys == "pretty okay":
        st.session_state['Scores'][2] = 4
    elif m_phys ==  "fit!":
        st.session_state['Scores'][2] = 5

    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)
 
# MENTAL ALERTNESS - 3
elif st.session_state['Current Page'] == 3:
    # st.write("MENTAL ALERTNESS")

    st.write("Alice and Bob have 420 cookies together. Bob has three times more cookies than Alice, how many cookies does he have?")
    m_mental_choice_1 = st.radio(
        label = "Choices",
        options = [
            "105", 
            "210",
            "315",
            "None of These"
            ]) # answer: 315

    st.write("Observe the pattern below:")
    st.info("64 | 60 | 58 | 52 | 44 | X")
    st.write("Which number can replace your X?")
    m_mental_choice_2 = st.radio(
        label="Choices", 
        options=[
            "36", 
            "30", 
            "40", 
            "28"
            ]) # answer: 30

    st.info('"DESPITE" | "IN SPITE OF"')
    st.write("The use of these phrases are...")
    m_mental_choice_3 = st.radio(
        label = "Choices", 
        options = [
            "Opposite", 
            "Similar", 
            "Unrelated to Each Other", 
            "None of the Above"
            ]) # answer: Similar

    # God abandoned me this way.
    st.session_state['Scores'][3] = 2
    # First Answer
    if m_mental_choice_1 == "315":
        st.session_state['Scores'][3] += 1
    # Second Answer
    if m_mental_choice_2 == "30":
        st.session_state['Scores'][3] += 1
    # Third Answer
    if m_mental_choice_3 == "Similar":
        st.session_state['Scores'][3] += 1
    
    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)

    # st.write("Questions based on https://www.jobtestprep.com/thurstone-test-mental-alertness") # just realized this would also reveal the answers KEK
 
# SELF CONFIDENCE - 4
elif st.session_state['Current Page'] == 4:
    # st.write("SELF CONFIDENCE")
    
    # item
    st.write("How confident do you see yourself?")
    m_conf = st.select_slider(
        label = "Slide to the prompt that best describes you", 
        options = (
            "I wish I am", 
            "Somewhat", 
            "Pretty much!", 
            "Definitely!"
            )
        )

    # God abandoned me this way.
    st.session_state['Scores'][4] = 0
    if m_conf == "I wish I am":
        st.session_state['Scores'][4] = 2
    elif m_conf == "Somewhat":
        st.session_state['Scores'][4] = 3
    elif m_conf == "Pretty much!":
        st.session_state['Scores'][4] = 4
    elif m_conf == "Definitely!":
        st.session_state['Scores'][4] = 5

    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)

# ABILITY TO PRESENT IDEAS - 5 
elif st.session_state['Current Page'] == 5:
    # st.write("ABILITY TO PRESENT IDEAS")

    st.write("Which of the following is an essential component of a well-structured presentation?")
    m_ideas_choice_1 = st.radio(
        label="Choices", 
        options = [
            "Clear introduction", 
            "Engaging visual aids", 
            "Concise conclusion", 
            "All of the above"
            ]) # Answer: All of the Above

    st.write("What is one of the recommended ways to maintain audience engagement during a presentation?")
    m_ideas_choice_2 = st.radio(
        label="Choices",
        options = [
            "Use exciting and colorful words", 
            "Incorporate storytelling techniques", 
            "Be controversial with your ideas", 
            "None of the above"
            ]) # Answer: "Incorporate storytelling techniques"

    st.write("You notice that some audience members appear disengaged during your presentation. What should you do?")
    m_ideas_choice_3 = st.radio(
        label = "Choices", 
        options = [
            "Increase your volume and speak louder to make them hear you", 
            "Use more complex technical terms to grab their attention", 
            "Pause and ask a question to encourage participation", 
            "Ignore them and continue with your presentation for those who are actually listening"
            ]) # Answer: Pause and ask a question to encourage participation

    # God abandoned me this way.
    st.session_state['Scores'][5] = 2
    # First Answer
    if m_ideas_choice_1 == "All of the above":
        st.session_state['Scores'][5] += 1
    # Second Answer
    if m_ideas_choice_2 == "Incorporate storytelling techniques":
        st.session_state['Scores'][5] += 1
    # Third Answer
    if m_ideas_choice_3 == "Pause and ask a question to encourage participation":
        st.session_state['Scores'][5] += 1

    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)

# COMMUNICATION SKILLS - 6
elif st.session_state['Current Page'] == 6:
    # st.write("COMMUNICATION SKILLS")

    m_comm_choice_1 = st.radio(
        label = "Which of the following is an essential component of effective communication?", 
        options = [
            "Active listening", 
            "Speaking slowly", 
            "Superior vocabulary", 
            "Using complex vocabulary"
            ]) # Answer: Active Listening

    m_comm_choice_2 = st.radio(
        label = "How would you handle a situation where you receive an email with unclear instructions?", 
        options = [
            "Ignore the email and wait for clarification.", 
            "Reply with your best guess.", 
            "Seek clarification by asking specific questions.", 
            "Reply with any response to buy time."
            ]) # Answer: Seek clarification by asking specific questions.

    m_comm_choice_3 = st.radio(
        label = "How would you handle a disagreement with a colleague during a team meeting?", 
        options = [
            "Assert your opinion.", 
            "Keep listening and avoid conflict.", 
            "Listen to their perspective and express your viewpoint respectfully.", 
            "Tell the issue to a supervisor."
            ]) # Answer:  "Listen to their perspective and express your viewpoint respectfully."

    # God abandoned me this way.
    st.session_state['Scores'][6] = 2
    # First Answer
    if m_comm_choice_1 == "Active listening":
        st.session_state['Scores'][6] += 1
    # Second Answer
    if m_comm_choice_2 == "Seek clarification by asking specific questions.":
        st.session_state['Scores'][6] += 1
    # Third Answer
    if m_comm_choice_3 == "Listen to their perspective and express your viewpoint respectfully.":
        st.session_state['Scores'][6] += 1

    next_button = st.button(label="Next",on_click=next)
    back_button = st.button(label="Back",on_click=prev)

# STUDENT PERFORMANCE RATING - 7
elif st.session_state['Current Page'] == 7:
    # st.write("STUDENT PERFORMANCE RATING")

    st.write("According to your University/School Record, what's your current GWA?")
    m_phys = st.select_slider(
        label = "Slide to the range that fits you", 
        options = (
            "below 3.00",
            "3.00-2.50", 
            "2.50-1.50", 
            "1.50-1.00"
            )
        )

    # God abandoned me this way.
    st.session_state['Scores'][7] = 0
    if m_phys == "below 3.00":
        st.session_state['Scores'][7] = 3
    elif m_phys == "3.00-2.50":
        st.session_state['Scores'][7] = 4
    elif m_phys == "2.50-1.50":
        st.session_state['Scores'][7] = 4
    elif m_phys == "1.50-1.00":
        st.session_state['Scores'][7] = 5

    back_button = st.button(label="Back",on_click=prev)
    submit_button = st.button(label="Submit", on_click=next)

# RESULTS - 8
elif st.session_state['Current Page'] == 8:
    st.write("YOUR RESULTS:")
    # predict here
    # st.session_state['Scores']
    
    
    results = predict_answers(
        st.session_state['Scores'][0],
        st.session_state['Scores'][1],
        st.session_state['Scores'][2],
        st.session_state['Scores'][3],
        st.session_state['Scores'][4],
        st.session_state['Scores'][5],
        st.session_state['Scores'][6],
        st.session_state['Scores'][7])
    # print(st.session_state['Scores'])
    if results == 0:
        st.header("Thank you for taking our Quiz!")
        st.divider()
        st.write("Unfortunately, according to our model, it looks like there are things you need to work on more... But don't worry! Our AI model is based on a dataset of only around 3000 entries and is not definitive of your full capabilities as a student")
        pass
        
    elif results == 1:
        st.header("Congratulations!")
        st.divider()
        st.write("According to our AI model, you have been deemed employable! Keep up the good work in being you!")
        pass
    # "pretend" to load here
    # if-else statement showing the appropriate response wherein if employable, say something like "Congratulations! Looks like you have what it takes to get a job! Omi job!"
    reset_button = st.button(label="Restart Quiz", on_click=reset_quiz)
    pass