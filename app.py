# importing libraies
from haystack.nodes import FARMReader
import streamlit as st
import time
from PIL import Image

# calling the model using FARMReader class
my_model = FARMReader(model_name_or_path="model")

img = Image.open('image.png')


# Function for fetching the answer to the context
def answering(ques, context):
    ans = my_model.predict_on_texts(ques, [context])
    ans = ans['answers'][0]
    if ans.score > .09:
        return ans.answer
    else:
        return 'Text is not enough for answering the Question.'


# Setting up the web app's icon and title
st.set_page_config(
    page_title="Question Answering System",
    page_icon=img,
    layout="centered",
    initial_sidebar_state="expanded"
)

# For hiding the menu icon in the top right part
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.title('Question Answering System')
# st.write("""##### Question Answering System will answer the questions based on the context given in the text area. The model is Build on RoBERTa Transformer and also fine tuned using Haystack library.""")
# st.write('')

text = st.text_area('Enter the Context')

question = st.text_input('Enter the Question')

button = st.button('Submit')

# here, passing the context and question from the text area to the function and showing the output.
if button:
    with st.spinner('PLease wait...'):
        time.sleep(.7)

    if text == '':
        st.write('## Please Enter the context')
    elif question == '':
        st.write('## Please Enter the question')
    else:
        answer = answering(question, text)
        if answer == 'Text is not enough for answering the Question.':
            st.write('## ' + answer)
        else:
            st.header('Answer:')
            st.write('## ' + answer)
