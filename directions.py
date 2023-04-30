import random

import main, utils, symbols


DEFAULT_ROUN = """
background-color:rgb(150, 175, 200);
color: rgb(75, 125, 175);
border:1px solid rgb(75,125,175);
"""

DEFAULT_UP = """
background-color:rgb(150, 175, 200);
color: rgb(75, 125, 175);
border:1px solid rgb(75,125,175);
border-bottom:none;
"""

DEFAULT_LEFT = """
background-color:rgb(150, 175, 200);
color: rgb(75, 125, 175);
border:1px solid rgb(75,125,175);
border-right:none;
"""

DEFAULT_RIGHT = """
background-color:rgb(150, 175, 200);
color: rgb(75, 125, 175);
border:1px solid rgb(75,125,175);
border-left:none;
"""

DEFAULT_DOWN = """
background-color:rgb(150, 175, 200);
color: rgb(75, 125, 175);
border:1px solid rgb(75,125,175);
border-top:none;
"""

WRONG_STYLE = """
background-color:rgb(177, 177, 188);
color: rgb(144, 144, 144);
"""

ANSWER_STYLE = """
color: rgb(100, 160, 125);
background-color: rgb(160, 190, 150);
"""

QUESTIONS = [
    ["제일 왼쪽에는 무엇이 있나요?", "left", [2]],
    ["왼쪽에는 무엇 무엇이 있나요?", "left", [0, 1, 2]],
    ["바로 왼쪽에는 무엇이 있나요?", "left", [0]],
    ["제일 오른쪽에는 무엇이 있나요?", "right", [2]],
    ["오른쪽에는 무엇 무엇이 있나요?", "right", [0, 1, 2]],
    ["바로 오른쪽에는 무엇이 있나요?", "right", [0]],
    ["제일 위에는 무엇이 있나요?", "up", [2]],
    ["위에는 무엇 무엇이 있나요?", "up", [0, 1, 2]],
    ["바로 위에는 무엇이 있나요?", "up", [0]],
    ["제일 아래에는 무엇이 있나요?", "down", [2]],
    ["아래에는 무엇 무엇이 있나요?", "down", [0, 1, 2]],
    ["바로 아래에는 무엇이 있나요?", "down", [0]],
]

DIRECTIONS = ["up", "down", "left", "right"]


quiz = []
answered = []
question = []


def initiate(ui):
    global quiz, answered, question
    answered = []
    question = random.choice(QUESTIONS)
    quiz = [question[1] + str(btn_no) for btn_no in question[2]]
    symbolz = random.sample(symbols.SYMB_NO_CONSEC, 4)

    ui.directions_roun.setStyleSheet(DEFAULT_ROUN)

    for i in range(0, 4):
        direction = DIRECTIONS[i]
        btn_symbols = random.sample(symbolz[i], 3)
        for x in range(0, 3):
            btn = getattr(ui, f"{direction}{x}")
            btn.setStyleSheet(globals()[f"DEFAULT_{direction.upper()}"])
            btn.setText(btn_symbols[x])

    ui.directions_quiz.setText(question[0])
    for i in range(0, 3):
        lbl = getattr(ui, f"dir_ans{i}")
        lbl.setText("")
    ui.directions_start.setEnabled(False)
    utils.play_tts("로운이의 " + question[0], kr=True)


def check_answer(ui, btn_name: str):
    btn_pressed = getattr(ui, btn_name)
    if btn_name in quiz and btn_name not in answered:
        lbl_index = len(answered)
        lbl_to_write = getattr(ui, f"dir_ans{lbl_index}")
        lbl_to_write.setText(btn_pressed.text())

        btn_pressed.setStyleSheet(
            globals()[f"DEFAULT_{btn_name[:-1].upper()}"] + ANSWER_STYLE
        )

        answered.append(btn_name)
        answered.sort()

        if answered == quiz:
            utils.playWOW()
            for i in range(0, 4):
                direction = DIRECTIONS[i]
                for x in range(0, 3):
                    btn_name = f"{direction}{x}"
                    btn = getattr(ui, btn_name)
                    if btn_name not in quiz:
                        btn.setStyleSheet(
                            globals()[f"DEFAULT_{direction.upper()}"] + WRONG_STYLE
                        )
                    else:
                        ui.directions_roun.setStyleSheet(DEFAULT_ROUN + ANSWER_STYLE)

            main.delay_time(ui, 1500)
            utils.play_tts("참 잘했어요!", kr=True)
            main.delay_time(ui, 2000)
            ui.directions_start.setEnabled(True)

    elif btn_name not in quiz:
        btn_pressed.setStyleSheet(
            globals()[f"DEFAULT_{question[1].upper()}"] + WRONG_STYLE
        )
