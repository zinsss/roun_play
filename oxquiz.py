import random

import main, utils

DEFAULT_QUIZ_STYLE = "color: rgb(50, 80, 80);"
O_QUIZ_STYLE = "color: rgb(77, 55, 177);"
X_QUIZ_STYLE = "color: rgb(133, 33, 33);"

O_STYLE = "color: rgb(100, 120, 180);"
X_STYLE = "color: rgb(200, 100, 100);"

O_BTN_STYLE = """
QPushButton {
	color: rgb(144, 166, 166);
    background: rgb(150, 170, 170);
    }
QPushButton:enabled {
	color: rgb(100, 120, 180);
    }
"""
X_BTN_STYLE = """
QPushButton {
	color: rgb(144, 166, 166);
    background: none;
}
QPushButton:enabled {
	color: rgb(200, 100, 100);
}
"""
WRONG_BTN_STYLE = "color:rgb(177, 177, 188);"

QUESTIONS = [
    ["엄마 이름은 차영.", True, "O", ""],
    ["엄마 차 파란색.", True, "O", ""],
    ["만촌동에 할머니 할아버지가 있어요.", True, "O", ""],
    ["아빠 이름은 이준성.", True, "X", "아빠 이름은 이진성이에요.."],
    ["1은 영어로 two.", True, "X", "1은 영어로 원.이에요."],
    ["아빠 차는 LEXUS", True, "X", "아빠 차는 미니에요."],
    ["로운이는 포항제일유치원을 다녀요.", True, "O", ""],
    ["오도리에 가면 바다가 있어요.", True, "O", ""],
    ["로운이 방에는 TV가 있어요.", True, "X", "로운이 방에 TV는 없어요."],
    ["지안이랑 유민이는 로운이 친구에요.", True, "O", ""],
    ["유치원 선생님 이름은 이유리.", True, "O", ""],
    ["사과는 보라색이에요.", True, "X", "사과는 빨간색이에요."],
    ["Two plus one equals, five.", False, "X", "Two plus one equals three."],
    ["이모 이름은 김지혜", True, "O", ""],
    ["로운이는 경선어린이집에 다녔어요.", True, "O", ""],
    ["할아버지 이름은 차두리", True, "X", "할아버지 이름은 차홍대에요."],
    ["율이 누나는 서울에 살아요.", True, "O", ""],
    ["아빠 차는 빨간색이에요.", True, "X", "아빠 차는 회색이에요."],
    ["사과는 빨간색.", True, "O", ""],
    ["Air My Fun은 재미있어요.", True, "O", ""],
    ["1 더하기 2는 3이에요.", True, "O", ""], 
    ["로운이 방에는 책상이 있어요.", True, "X", "로운이 방에 책상은 없어요."],
    ["로운이는 포항제일유치원 우주반이에요.", True, "X", "혜성반이에요!!"],
    ["기도 마지막에는 아멘.이라고 말해요", True, "O", ""],
    ["기도할때는 시끄럽게 놀아도 되요", True, "X", "기도할땐 조용히."],
    ["Five is bigger than seven.", False, "X", "Five is smaller than seven."]
]

quiz = []
initiated = False


def start_game(ui):
    global quiz, initiated
    quiz = random.choice(QUESTIONS)
    initiated = True

    ui.ox_quiz.setStyleSheet(DEFAULT_QUIZ_STYLE)
    ui.ox_quiz.setText(quiz[0])

    ui.O_btn.setStyleSheet(O_BTN_STYLE)
    ui.X_btn.setStyleSheet(X_BTN_STYLE)

    utils.play_tts(quiz[0], kr=quiz[1])

    ui.ox_start.setEnabled(False)
    ui.ox_tts.setEnabled(True)
    ui.O_btn.setEnabled(True)
    ui.X_btn.setEnabled(True)


def check_answer(ui, ox: str):
    global quiz, initiated
    if quiz[2] != ox:
        btn_pressed = getattr(ui, f"{ox}_btn")
        btn_pressed.setStyleSheet(WRONG_BTN_STYLE)
    else:
        ui.ox_answer.setStyleSheet(globals()[f"{ox}_STYLE"])
        ui.ox_answer.setText(quiz[2])
        ui.ox_quiz.setStyleSheet(globals()[f"{ox}_QUIZ_STYLE"])
        main.delay_time(ui, 200)
        utils.playWOW()
        print("wow")
        main.delay_time(ui, 2000)
        if quiz[2] == "O":
            if quiz[1]:
                utils.play_tts("네!"+quiz[0], kr=quiz[1])
            else: utils.play_tts("Yes" + quiz[0], kr=quiz[1])
        else:
            if quiz[1]:
                utils.play_tts("아니오!"+quiz[3], kr=quiz[1])
            else: utils.play_tts("No," + quiz[3], kr=quiz[1])
        main.delay_time(ui, 5000)

        ui.ox_answer.setText("")
        ui.ox_quiz.setText("")
        ui.ox_start.setEnabled(True)
        ui.ox_tts.setEnabled(False)
        ui.O_btn.setEnabled(False)
        ui.X_btn.setEnabled(False)

        initiated = False
