import random
from PySide6.QtGui import QPixmap
import main, utils

QUIZ_LE_STYLE = """
border:none;
background-color:rgb(100, 150, 160);
border-radius:25px;
color: rgb(200, 160, 100);
"""

DEFAULT_LE_STYLE = """
border:none;
background-color:rgb(120, 150, 160);
border-radius:25px;
color: rgb(200, 180, 100);
"""

alphabet_selected = False

phonics_word = ""
quiz = ""
quiz_index = 0


def new_game(ui):
    global alphabet_selected
    alphabet_selected = False
    ui.eng1_alphabet.setText("")
    ui.eng1_alphabet.setReadOnly(False)
    for i in range(0, 9):
        le = getattr(ui, f"eng1_spell_{i}")
        le.setStyleSheet(DEFAULT_LE_STYLE)
        le.setText("")
        le.setReadOnly(True)

    ui.eng1_img.clear()
    ui.eng1_img.setText("Phonics\nLets play!")


def load_phonics(ui, phonics):
    PHONICS_A = ["ambulance", "apple"]
    PHONICS_B = ["balloon", "basket", "book", "boy"]
    PHONICS_C = ["cat", "chair", "christmas", "cow"]
    PHONICS_D = ["dance", "down"]
    PHONICS_E = ["elephant"]
    PHONICS_F = ["flower", "friends"]
    PHONICS_G = ["gloves"]
    PHONICS_H = ["hands", "hat", "hug"]
    PHONICS_I = ["ice"]
    PHONICS_J = ["jellyfish", "jump"]
    PHONICS_K = ["keyboard", "koala"]
    PHONICS_L = ["ladybug", "lamp"]
    PHONICS_M = ["mango", "mask"]
    PHONICS_N = ["night", "numbers"]
    PHONICS_O = ["oh_my_god", "octopus"]
    PHONICS_P = ["pancake", "pillow"]
    PHONICS_Q = ["question", "quiet"]
    PHONICS_R = ["robot", "rocket"]
    PHONICS_S = ["school", "spider"]
    PHONICS_T = ["telephone", "tiger"]
    PHONICS_U = ["umbrella", "unicorn", "up"]
    PHONICS_V = ["violin", "volcano"]
    PHONICS_W = ["walking", "wave"]
    PHONICS_X = ["xylophone"]
    PHONICS_Y = ["yawn", "yogurt"]
    PHONICS_Z = ["zoo"]

    global alphabet_selected, phonics_word
    alphabet_selected = True
    ui.eng1_alphabet.setReadOnly(True)
    alphabet = phonics.upper()
    phonics_list = locals()[f"PHONICS_{alphabet}"]
    phonics_word = random.choice(phonics_list)
    word = utils.sliceword(phonics_word)

    ui.eng1_img.setPixmap(QPixmap(f"resources/eng1/{phonics_word}.jpg"))

    for i in range(len(word)):
        le = getattr(ui, f"eng1_spell_{i}")
        if word[i] != "_":
            le.setText(word[i])
        else:
            le.setText(" ")

    global quiz, quiz_index
    quiz_index = random.randint(0, len(word) - 1)
    quiz = word[quiz_index]
    while quiz == "_":
        quiz_index = random.randint(0, len(word) - 1)
        quiz = word[quiz_index]

    quiz_le = getattr(ui, f"eng1_spell_{quiz_index}")
    quiz_le.setText("")
    quiz_le.setReadOnly(False)
    quiz_le.setStyleSheet(QUIZ_LE_STYLE)
    quiz_le.setFocus()


def check_answer(ui, alphabet):
    if alphabet == "":
        return
    elif alphabet == quiz:
        quiz_le = getattr(ui, f"eng1_spell_{str(quiz_index)}")
        quiz_le.setReadOnly(True)
        ui.messages.setText("참 잘했어요!!")
        main.delay_time(ui, 100)
        utils.playWOW()
        main.delay_time(ui, 1500)
        utils.play_tts(phonics_word)
        main.delay_time(ui, 4000)
        new_game(ui)


def keyb(ui, key):
    alphabet = ui.eng1_alphabet
    quiz_le = getattr(ui, f"eng1_spell_{str(quiz_index)}")
    if alphabet_selected:
        quiz_le.setFocus()
    else:
        alphabet.setFocus()
    utils.press_key(ui, key)
