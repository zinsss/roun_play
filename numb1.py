import random
from PySide6.QtCore import Qt, QUrl

import main, utils

numb1_answer = 0
numb1_quiz = 0

QUIZ_STYLE = """
border:none;
background-color:rgb(100, 150, 160);
border-radius:50px;
color: rgb(200, 160, 100);
"""

DEFAULT_STYLE = """
border:none;
background-color:rgb(120, 150, 160);
border-radius:50px;
color: rgb(200, 180, 100);
"""


def new_game(ui):
    first_number = random.randint(0, 95)

    global numb1_answer, numb1_quiz
    numb1_quiz = random.randint(0, 4)
    numb1_answer = first_number + numb1_quiz

    for n in range(0, 5):
        le = getattr(ui, f"numb1_{n}")
        le.setText(str(first_number + n))
        le.setStyleSheet(DEFAULT_STYLE)

    quiz = getattr(ui, f"numb1_{numb1_quiz}")
    quiz.setText("")
    quiz.setStyleSheet(QUIZ_STYLE)
    quiz.setReadOnly(False)
    quiz.setFocusPolicy(Qt.StrongFocus)
    quiz.setFocus()


def check_answer(ui, answ):
    dis_enable_btns = [ui.n1_clr_btn, ui.n1_new_btn, ui.n1_bs_btn]
    quiz = getattr(ui, f"numb1_{numb1_quiz}")
    if answ == "":
        return
    if int(answ) == numb1_answer:
        quiz.setReadOnly(True)
        for btn in dis_enable_btns:
            btn.setEnabled(False)
        ui.messages.setText("참 잘했어요!!")
        main.delay_time(ui, 100)
        utils.playWOW()
        main.delay_time(ui, 3000)
        new_game(ui)
        for btn in dis_enable_btns:
            btn.setEnabled(True)


def clear_quiz(ui):
    quiz = getattr(ui, f"numb1_{numb1_quiz}")
    quiz.setText("")
    quiz.setFocus()


def keyb(ui, key):
    quiz = getattr(ui, f"numb1_{numb1_quiz}")
    quiz.setFocus()
    utils.press_key(ui, key)
