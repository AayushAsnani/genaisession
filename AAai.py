import streamlit as st
import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
genai.configure(api_key="AIzaSyBBuObGEj8EVmsOdn0sNMWynk6WYeSp-2Y")
mymodel = genai.GenerativeModel('gemini-1.5-flash')
chat = mymodel.start_chat()
engine = pyttsx3.init()

st.header("What's On Your Mind Today")
question = st.text_input("Search Here")
if st.button("search:"):
    st.write("Here's what you need:")
    response1 = mymodel.generate_content(question)
    st.write("Results:", response1.text)
if st.button("voice"):
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
           st.write("say something!")
           audio = r.listen(source)
        question = r.recognize_google(audio)
        st.write("you asked:" + question)
        response = chat.send_message(question)
        st.write("Gemini:",response.text)
        engine.say(response.text)
        engine.runAndWait()
    except:
        st.write("problem with getting audio input")
