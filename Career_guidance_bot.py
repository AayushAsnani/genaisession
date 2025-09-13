import google.generativeai as genai
genai.configure(api_key="AIzaSyBBuObGEj8EVmsOdn0sNMWynk6WYeSp-2Y")
mymodel = genai.GenerativeModel('gemini-1.5-flash')
chat = mymodel.start_chat()
while True:
    q1= input("what are you pursuing currently: ")
    q2 = input("your salary expectations: ")
    q3 = input("your point of interest")
    question =f"""
Give me career guidance ,i am a student pursuing{q1},my salary expectations are{q2},i need to build a career in {q3}"""
    response = chat.send_message(question)
    print("Gemini:",response.text)