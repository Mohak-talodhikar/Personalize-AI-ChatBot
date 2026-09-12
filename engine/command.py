import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand(timeout=10, phrase_time_limit=8):
    r = sr.Recognizer()
    
    # Lower threshold = more sensitive to normal voice
    r.energy_threshold = 1000
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1.0
    
    print("\nListening... (speak now)")
    eel.DisplayMessage("Listening...")
    
    try:
        with sr.Microphone() as source:
            # Listen longer for ambient noise so voice is clear
            print("Adjusting for background noise... please wait")
            r.adjust_for_ambient_noise(source, duration=1)
            print(f"Energy threshold set to: {r.energy_threshold}")
            
            try:
                # Longer timeout so you get time to start speaking
                audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                
                print("Recognizing...")
                eel.DisplayMessage("Recognizing...")
                
                # Try Google Web Speech API
                try:
                    query = r.recognize_google(audio, language='en-in')
                    print(f"You said: {query}")
                    eel.DisplayMessage(query)
                    return query.lower().strip()
                    
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                    return ""
                    
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")
                    return ""
                
            except sr.WaitTimeoutError:
                print("No speech detected within the timeout period.")
                eel.DisplayMessage("I didn't hear you. Click mic again and speak louder / closer.")
                return ""
                
    except OSError as e:
        print(f"Microphone error: {e}")
        print("Please check if your microphone is properly connected.")
        eel.DisplayMessage("Microphone not found")
        return ""
        
    except Exception as e:
        print(f"Unexpected error in speech recognition: {e}")
        return ""
    
    return ""


@eel.expose
def allCommands(message=1):

#   query = takecommand() this query is getting message from mic
    if message == 1:
        query = takecommand() 
        print(query)
        eel.senderText(query)
    else:
#   eel.senderText(query) this query is getting message from  chatbox
        query = message
        eel.senderText(query)
    
    try:
        if "open" in query and "youtube" not in query:
            from engine.features import openCommand
            openCommand(query)
        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")
    
    eel.ShowHood()
    