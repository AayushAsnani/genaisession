import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
genai.configure(api_key="AIzaSyBBuObGEj8EVmsOdn0sNMWynk6WYeSp-2Y")
mymodel = genai.GenerativeModel('gemini-1.5-flash')
chat = mymodel.start_chat()
engine = pyttsx3.init()


while True:
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
           print("say something!")
           audio = r.listen(source)
        question = r.recognize_google(audio)
        if question == "stop":
            break
        print("you asked:" + question)
        response = chat.send_message(question)
        print("Gemini:",response.text)
        engine.say(response.text)
        engine.runAndWait()
    except:
        print("problem with getting audio input")
