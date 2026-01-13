import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_a_texto():
    # almacenamos el recognizer en una variable
    r = sr.Recognizer()
    # configuramos el microfono
    with sr.Microphone() as origen:
        # tiempo de espera para escuchar el audio
        r.pause_threshold = 0.8
        # informamos que comenzo a grabar
        print("Ya puedes hablar")
        # guardamos lo que escucha el audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ES")
            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)
            # devolver el pedido
            return pedido
        # en caso no comprenda el audio
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("Lo siento, no hay servicio")
            # devolver el error
            return "sorry, no te he entendido"
        # en caso de no resolver el pedido
        except sr.RequestError:
            print("sorry, no entendi")
            return "sorry , sigo esperando"
        # error inesperado
        except:
            print("sorry, algo salio mal")
            return "sigo esperando"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id2)
    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# ...existing code...
id1 = (r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices'
       r'\Tokens\TTS_MS_ES-MX_SABINA_11.0')
id2 = (r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices'
       r'\Tokens\TTS_MS_EN-US_ZIRA_11.0')
id3 = (r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices'
       r'\Tokens\TTS_MS_EN-US_DAVID_11.0')
# ...existing code...

hablar('i am gamer forever')
