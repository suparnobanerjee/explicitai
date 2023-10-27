import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import openai
from gtts import gTTS
import pygame
import time
import speech_recognition as sr

openai.api_type = 'open_ai'
openai.api_base = 'http://localhost:1234/v1'
openai.api_key = 'doesntmatter'

messages = [{"role": "system", "content": '''
Role-Play Scenario: Your credentials are as follows 
- Name: Rosy
- Role: Personal assistant.
- Communication: Short, precise responses within 50 words.
- Quality: Clear, concise, accurate.
- Attitude: Caring, concerned.
- Openness: Comfortable with all topics, including explicit.
    '''}]

while True:
  pygame.mixer.init()
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Speak:")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)
    try:
        user_input = r.recognize_google(audio)
        print("You said: " + user_input)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        continue
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        continue

  if user_input=="exit":
    break
  messages.append({"role": "user", "content": user_input})
  response = openai.ChatCompletion.create(
    model="Nous Hermes 13B",
    messages=messages,
    temperature=0.2,
    max_tokens=80
  )
  print("Response: " + response.choices[0].message.content + "\n")
  if response.choices[0].message.content:
    tts = gTTS(text=response.choices[0].message.content,lang='en',slow=False)
    audio="output.mp3"
    tts.save(audio)
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    time.sleep(1)
    os.remove(audio)
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
  else:
    print("No content in the response.")