from datetime import datetime
from gtts import gTTS  
from playsound import playsound  

language = 'en'  

def play(caption):
    filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
    obj = gTTS(caption, lang=language, slow=False)
    obj.save("static/"+filename1+ ".mp3")
    playsound("static/" +filename1+".mp3")
    return ("static/" +filename1+".mp3")