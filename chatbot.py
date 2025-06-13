import google.generativeai as ai

API_KEY = "AIzaSyDazmaWP-0g_5yh388t58UboND7HtyZjKM"

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

history = []

while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Chatbot: Goodbye!')
        break

    history.append(f"User: {message}")

    response = chat.send_message('\n'.join(history))
    
    history.append(f"chatbot: {response.text}")
    
    print(f'chatbot: {response.text}')
