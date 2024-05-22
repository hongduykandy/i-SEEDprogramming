####Assignment 10

from gtts import gTTS
from playsound import playsound

# Text to speech
text = "Hello, This is the place where you can fill in text to change it to speech."
language = 'en'
output = gTTS(text=text, lang=language, slow=False)
output.save("audio_output.mp3")

#Play the output
playsound("audio_output.mp3")