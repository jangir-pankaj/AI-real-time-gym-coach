from io import BytesIO
from gtts import gTTS

class TextToSpeech:
    def speak(self,text,lang="en"):

        cleaned_text = (text or "").strip()

        if not cleaned_text:
            return
        
        buffer = BytesIO()
        gTTS(text=cleaned_text,lang=lang,).write_to_fp(buffer)
        buffer.seek(0)

        return buffer.read()