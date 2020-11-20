import pyttsx3
engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.runAndWait()

print(id(engine))
engine2 = pyttsx3.init()
print(id(engine2))