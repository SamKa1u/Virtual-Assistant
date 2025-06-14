import assemblyai as aai
import speech_recognition as sr
# from assemblyAPI import assemblyai_APIKey

api_key = 'abf4f1876b0f41c2b3a04377b71eb01e'#assemblyai_APIKey()
# set the API key
aai.settings.api_key = f"{api_key}"

def STT():
    r = sr.Recognizer()
    transcriber = aai.Transcriber()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        audio_data = audio.get_wav_data()

    try:
        print("Recognizing...")
        query = transcriber.transcribe(audio_data)
        print(f"User said: {query.text}\n")
        q1 = query.text
        q = q1.replace('.','')
    except Exception as e:
        print(e)
        print("Unable to ascertain query")
        return None

    return q

if __name__ == "__main__":
    response = STT()
