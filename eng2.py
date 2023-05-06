import os
import random
from PySide6.QtGui import QPixmap
import main, utils


btn_words = []
quiz_index = 0

ANSWER_STYLE = """
color: rgb(50, 125, 175);
"""

WRONG_STYLE = """
color: rgb(200, 120, 75);
"""

DEFAULT_BORDER_STYLE = """
border:3px solid rgb(120,150,120);
"""

ANSWER_BORDER_STYLE = """
border:3px solid rgb(75,125,175);
"""

WRONG_BORDER_STYLE = """
border:3px solid rgb(180,80,80);
"""


def new_game(ui):
    files = os.listdir("resources/eng2")
    words = []
    for file in files:
        if file != 'mp3':
            word_temp = file.replace(".jpg", "")
            word = word_temp.replace("_", " ")
            words.append(word)
        else:
            pass 

    global btn_words, quiz_index
    btn_words = random.sample(words, 5)
    quiz_index = random.randint(0, 4)
    for i in range(0, 5):
        btn = getattr(ui, f"eng2_ans{i}")
        lbl = getattr(ui, f"eng2_ansLbl_{i}")
        btn.setStyleSheet(DEFAULT_BORDER_STYLE)
        lbl.setText("")

    ui.eng2_word.setText(btn_words[quiz_index])
    for i in range(0, 5):
        btn = getattr(ui, f"eng2_ans{i}")
        btn_word = btn_words[i].replace(" ", "_")
        btn.setIcon(QPixmap(f"resources/eng2/{btn_word}"))


def check_answer(ui, btn_index):
    if btn_words[btn_index] == btn_words[quiz_index]:
        for i in range(0, 5):
            lbl = getattr(ui, f"eng2_ansLbl_{i}")
            btn = getattr(ui, f"eng2_ans{i}")
            lbl.setText(btn_words[i])
            if i == btn_index:
                lbl.setStyleSheet(ANSWER_STYLE)
                btn.setStyleSheet(ANSWER_BORDER_STYLE)
            else:
                lbl.setStyleSheet(WRONG_STYLE)
                btn.setStyleSheet(WRONG_BORDER_STYLE)
        ui.messages.setText("참 잘했어요!!")
        main.delay_time(ui, 100)
        utils.playWOW()
        main.delay_time(ui, 3000)
        mp3filename = btn_words[quiz_index].replace(" ", "_")
        utils.play_MP3("resources/eng2/mp3/" + mp3filename + ".mp3")
        main.delay_time(ui, 1000)
        new_game(ui)
    else:
        lbl = getattr(ui, f"eng2_ansLbl_{btn_index}")
        btn = getattr(ui, f"eng2_ans{btn_index}")
        lbl.setText(btn_words[btn_index])
        lbl.setStyleSheet(WRONG_STYLE)
        btn.setStyleSheet(WRONG_BORDER_STYLE)
