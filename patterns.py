import random

import main, utils, symbols


PATTERNS = [
    [[0, 1, 0, 1, 0, 1], 0],
    [[0, 1, 2, 0, 1, 2], 0],
    [[0, 1, 2, 3, 0, 1], 2],
    [[0, 1, 2, 3, 4, 0], 1],
    [[0, 1, 1, 0, 1, 1], 1],
    [[0, 1, 1, 1, 0, 1], 1],
    [[0, 1, 1, 1, 1, 0], 1],
]

DEFAULT_LBL_STYLE = """
color: rgb(100, 150, 125);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-right:none;
"""
LBL_STYLE_0 = """
color: rgb(100, 160, 125);
background-color: rgb(160, 190, 150);
border:10px solid rgb(50, 80, 75);
border-right:none;
"""
LBL_STYLE_1 = """
color: rgb(188, 166, 50);
background-color: rgb(200, 188, 122);
border:10px solid rgb(50, 80, 75);
border-right:none;
border-left:1px solid rgb(50, 80, 75);
"""
LBL_STYLE_2 = """
color: rgb(180, 100, 100);
background-color: rgb(200, 155, 155);
border:10px solid rgb(50, 80, 75);
border-right:none;
border-left:1px solid rgb(50, 80, 75);
"""
LBL_STYLE_3 = """
color: rgb(150, 120, 160);
background-color: rgb(175, 155, 190);
border:10px solid rgb(50, 80, 75);
border-right:none;
border-left:1px solid rgb(50, 80, 75);
"""
LBL_STYLE_4 = """
color: rgb(122, 100, 100);
background-color: rgb(166, 144, 144);
border:10px solid rgb(50, 80, 75);
border-right:none;
border-left:1px solid rgb(50, 80, 75);
"""

LBL_STYLES = [LBL_STYLE_0, LBL_STYLE_1, LBL_STYLE_2, LBL_STYLE_3, LBL_STYLE_4]

DEFAULT_BTN_STYLE = """
background-color:rgb(150, 175, 200);
color: rgb(75, 125, 175);
border:1px solid rgb(75,125,175);
border-radius:20px;
"""

WRONG_BTN_STYLE = """
background-color:rgb(175, 175, 175);
color: rgb(150,150,150);
border:1px solid rgb(150,150,150);
border-radius:20px;
"""

ANSWER_BTN_STYLE = """
background-color:rgb(125, 175, 220);
color: rgb(50, 150, 200);
border:3px solid rgb(50, 150, 200);
border-radius:20px;
"""

DEFAULT_Q_STYLE = """
color: rgb(50, 150, 25);
background-color: rgb(150, 175, 125);
border:3px solid rgb(125,150,100);
"""


quiz = ""
quiz_pattern = []


def initiate(ui):
    global quiz, quiz_pattern
    symbls = random.choice(symbols.SYMB_NO_CONSEC)
    quiz_symbs = random.sample(symbls, 5)
    quiz_pattern = random.choice(PATTERNS)

    ui.pttQ.setStyleSheet(DEFAULT_Q_STYLE)
    ui.pttQ.setText("?")

    for i in range(0, 6):
        lbl = getattr(ui, f"ptt{i}")
        lbl.setText(quiz_symbs[quiz_pattern[0][i]])
        lbl.setStyleSheet(DEFAULT_LBL_STYLE)

    quiz = quiz_symbs[quiz_pattern[1]]

    btn_symbs = random.sample(quiz_symbs, 3)
    while quiz in btn_symbs:
        btn_symbs = random.sample(quiz_symbs, 3)
    quiz_index = random.randint(0, 3)
    btn_symbs.insert(quiz_index, quiz)
    for x in range(0, 4):
        btn = getattr(ui, f"ptt_ans{x}")
        btn.setText(btn_symbs[x])
        btn.setStyleSheet(DEFAULT_BTN_STYLE)


def check_answer(ui, btn_no: int, symb: str):
    if symb == quiz:
        for i in range(0, 6):
            lbl = getattr(ui, f"ptt{i}")
            lbl.setStyleSheet(LBL_STYLES[quiz_pattern[0][i]])

        for x in range(0, 4):
            btn = getattr(ui, f"ptt_ans{x}")
            if x == btn_no:
                btn.setStyleSheet(ANSWER_BTN_STYLE)
            else:
                btn.setStyleSheet(WRONG_BTN_STYLE)

        ui.pttQ.setStyleSheet(LBL_STYLES[quiz_pattern[1]])
        ui.pttQ.setText(symb)

        utils.playWOW()

        main.delay_time(ui, 7000)
        initiate(ui)
    else:
        btn = getattr(ui, f"ptt_ans{btn_no}")
        btn.setStyleSheet(WRONG_BTN_STYLE)
