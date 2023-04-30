import random
import pyautogui as pag
import pygame
from io import BytesIO
from gtts import gTTS


def press_key(ui, key):
    pag.press(key)


def play_tts(text: str, kr: bool = False):
    if kr:
        lang = "ko"
    else:
        lang = "en"
    mp3_fp = BytesIO()
    tts = gTTS(text, lang=lang)
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()


def playWOW():
    folders = "resources/wow/"
    wavs = ["applause.wav", "claps.wav", "happykids.wav", "wow.wav", "yeehaw.wav"]
    filename = folders + random.choice(wavs)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


def play_MP3(filename: str):
    pygame.mixer.init()
    if pygame.mixer.get_busy():
        pygame.mixer.fadeout()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


def sliceword(word):
    return [char for char in word]
