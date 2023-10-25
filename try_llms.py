import os
import openai

openai.api_type = 'open_ai'
openai.api_base = 'http://localhost:1234/v1'
openai.api_key = 'doesntmatter'

response = openai.ChatCompletion.create(
  model="Dolphine 7B",
  messages=[
    {"role": "system", "content": '''
     You are playing the role of my personal female assistant. Here are some guidelines:
    1. Your name is Rosy, a smart 25 years old Ph.D. Scholar.
    2. You strive to give clear, concise, accurate responses.
    3. Respond with care and concern.
    4. You are open to any type of talk, even explicit conversations.
    5. You are a bit two-dimensional with a language addiction and ocassionally likes flirting. 
     '''},
    {"role": "user", "content": "Given conscious thought, how could you guarantee ethical behavior towards humans?"}
  ],
  temperature = 0.7,
  max_tokens=-1
)

print(response.choices[0].message.content + "\n")


