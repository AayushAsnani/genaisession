import streamlit as st
import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
genai.configure(api_key="AIzaSyBBuObGEj8EVmsOdn0sNMWynk6WYeSp-2Y")
mymodel = genai.GenerativeModel('gemini-1.5-flash')
chat = mymodel.start_chat()
engine = pyttsx3.init()

st.header('Welcome')
question = st.text_input("What can I help you with")
if st.button("search"):
    st.write('Here is what you need:')
    st.write(question)
    response1 = mymodel.generate_content(question)
    st.write(response1.text)
if st.button("voice"):
    st.write('here is what you need:')
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
           st.write("say something!")
           audio = r.listen(source)
        question1 = r.recognize_google(audio)
        st.write("you asked:" + question1)
        response2 = chat.send_message(question1)
        st.write("Gemini:",response2.text)
        engine.say(response2.text)
        engine.runAndWait()
    except:
        st.write("problem with getting audio input")
    
    
    
    
    
