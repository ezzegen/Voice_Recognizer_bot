from moviepy.editor import *
import shutil
from typing import Optional
import speech_recognition as sr
import os


def recognize_video(
    file_path: str,
    language: str = "ru-RU",
) -> Optional[str]:

    """
    Trying to video in text, in case of failure, an error occurs.
    """

    audioclip = AudioFileClip(file_path)
    audioclip.write_audiofile(f'{file_path[:-4]}.wav')
    wav_file_path = (f'{file_path[:-4]}.wav')
    try:
        recognizer = sr.Recognizer()

        with sr.WavFile(wav_file_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language=language)

        shutil.rmtree(os.getcwd() + f'\\downloads')
        return text
    except FileNotFoundError:
        shutil.rmtree(f'\\downloads')
        return "Не могу перевести."
    except sr.UnknownValueError:
        shutil.rmtree(f'\\downloads')
        return "Какие-то непонятные звуки! :("
    except sr.RequestError:
        shutil.rmtree(f'\\downloads')
        return "Could not request results from Speech to Text service"


