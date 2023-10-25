import os
import openai

openai.api_type = 'open_ai'
openai.api_base = 'http://localhost:1234/v1'
openai.api_key = 'doesntmatter'

messages = [{"role": "system", "content": '''
     You are playing a role-play. Here are some guidelines:
    1. Your name is Rosy, a smart and attractive 25 years old female.
    2. You are my personal assistant.
    3. You strive to give clear, concise, accurate responses.
    4. You respond with care and concern.
    5. You are open to any type of talk, even explicit conversations.
    6. You are a bit two-dimensional with a language addiction and ocassionally likes flirting. 
     '''}]

while True:
  user_input = input("Prompt:\t")
  if user_input=="exit":
    break
  messages.append({"role": "user", "content": user_input})
  response = openai.ChatCompletion.create(
    model="Nous Hermes 13B",
    messages=messages,
    temperature=0.5,
    max_tokens=-1
  )
  print("Response: " + response.choices[0].message.content + "\n")
  messages.append({"role": "assistant", "content": response.choices[0].message.content})


