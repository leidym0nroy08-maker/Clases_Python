import pyttsx3

nombre = input ("¿como te llamas?") 

motor = pyttsx3.init()
voces = motor.getProperty ('voices')
motor.setProperty('voice', voces [0].id)

motor.say(f"Hola {nombre},esta es mi nueva voz")
motor.runAndWait()