from env import secret
from openai import OpenAI
import os

# Add response of chat to the history

def call_chatgpt(message):

    client = OpenAI(api_key=secret)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=message,
        max_tokens=150,
        temperature=0.7,
    )

    return response.choices[0].message.content

    with open('chathist.txt', 'w') as file:
        pass

def pat_ppt(user_input):


    with open('chathist.txt', 'r') as file:
        file_content = file.read()
        # print(file_content)


    chat_hist = ''
    chat_chat_hist = ''
    chat_response = ''





    with open('chathist.txt', 'r') as file:
        file_content = file.read()
        # print(file_content)

    # 1. create a chat_hist variable
    # 2. pass chat_hist to prompt
    # 3, reset var
    # print("Chat hist before input = ", chat_hist)

    if chat_hist != user_input:
        chat_hist = user_input

    if chat_chat_hist != chat_response:
        chat_chat_hist = chat_response




    # print("user input = ", user_input)
    # print("Chat hist after input= ", chat_hist)

    prompt = [{
        "role": "system",
        "content": user_input +  " This is all the previous questions I have asked, and the answers you gave me: " + file_content,
        }]

    # print("prompt = ", prompt)

    chat_response = call_chatgpt(prompt)

    with open('chathist.txt', 'a') as file:
        file.write(user_input + '\n This was your response: ' + chat_response + '\n')

    user_input = user_input
    return chat_response

