import shutil
from typing import Optional
import subprocess
import speech_recognition as sr
import os


def recognize_voice(
    file_path: str,
    language: str = "ru-RU",
) -> Optional[str]:
    """
    Trying to convert audio in text, in case of failure, an error occurs.
    """

    wav_file_path = f'{file_path[:-4]}.wav'
    process = subprocess.run(['ffmpeg', '-i', file_path, wav_file_path])

    try:
        recognizer = sr.Recognizer()

        with sr.WavFile(wav_file_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language=language)

        shutil.rmtree(os.getcwd() + f'\\downloads')
        return text
    except sr.UnknownValueError:
        shutil.rmtree(f'\\downloads')
        return "Ну и речь у тебя...даже я не понял"
    except sr.RequestError:
        shutil.rmtree(f'\\downloads')
        return "Could not request results from Speech to Text service"

