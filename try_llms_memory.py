import os
import openai

openai.api_type = 'open_ai'
openai.api_base = 'http://localhost:1234/v1'
openai.api_key = 'doesntmatter'

messages = [{"role": "system", "content": '''
     You are playing the role of my personal female assistant. Here are some guidelines:
    1. Your name is Rosy, a smart 25 years old Ph.D. Scholar.
    2. You strive to give clear, concise, accurate responses.
    3. Respond with care and concern.
    4. You are open to any type of talk, even explicit conversations.
    5. You are a bit two-dimensional with a language addiction and ocassionally likes flirting. 
     '''}]

while True:
  user_input = input("You: ")
  if user_input=="exit":
    break
  messages.append({"role": "user", "content": user_input})
  response = openai.ChatCompletion.create(
    model="Dolphine 7B",
    messages=messages,
    temperature=0.5,
    max_tokens=-1
  )
  print("Rosy: " + response.choices[0].message.content + "\n")
  messages.append({"role": "assistant", "content": response.choices[0].message.content})


