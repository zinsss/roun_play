import random
from PySide6.QtGui import QPixmap
import main, utils

DEFAULT_STYLE = """
background-color: rgb(190, 200, 160);
border:none;
border-radius:20px;
color:rgb(75, 150, 125);
"""

SELECTED_STYLE = """
background-color: rgb(160, 200, 140);
border:none;
border-radius:20px;
color:rgb(75, 125, 25);
"""

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

NUMB_WORDS = [
    ["zero", "공, 영"],
    ["one", "일, 하나"],
    ["two", "이, 둘"],
    ["three", "삼, 셋"],
    ["four", "사, 넷"],
    ["five", "오, 다섯"],
    ["six", "육, 여섯"],
    ["seven", "칠, 일곱"],
    ["eight", "팔, 여덟"],
    ["nine", "구, 아홉"],
    ["ten", "십, 열"],
    ["eleven", "십일, 열하나"],
    ["twelve", "십이, 열둘"],
    ["thirteen", "십삼, 열셋"],
    ["fourteen", "십사, 열넷"],
    ["fifteen", "십오, 열다섯"],
    ["sixteen", "십육, 열여섯"],
    ["seventeen", "십칠, 열일곱"],
    ["eighteen", "십팔, 열여덟"],
    ["nineteen", "십구, 열아홉"],
    ["twenty", "이십, 스물"],
]

currentNumber = ""
quiz = ""
quiz_index = 0


def new_game(ui, numb: int):
    for i in range(0, 9):
        le = getattr(ui, f"numb3_le_{i}")
        le.setStyleSheet(DEFAULT_LE_STYLE)
        le.setText("")
        le.setReadOnly(True)
    for i in range(0, 21):
        btn = getattr(ui, f"numb3_no_{i}")
        btn.setStyleSheet(DEFAULT_STYLE)

    ui.numb3_numb.setText(str(numb))
    current_btn = getattr(ui, f"numb3_no_{numb}")
    current_btn.setStyleSheet(SELECTED_STYLE)
    ui.numb3_numb_kor.setText(NUMB_WORDS[numb][1])
    ui.numb3_img1.setPixmap(QPixmap(f"resources/numb3/numberblocks/{str(numb)}.jpg"))
    ui.numb3_img2.setPixmap(QPixmap(f"resources/numb3/images/{str(numb)}.jpg"))

    numb_spelling = utils.sliceword(NUMB_WORDS[numb][0])
    global currentNumber, quiz, quiz_index
    currentNumber = numb
    quiz_index = random.randint(0, len(numb_spelling) - 1)
    quiz = numb_spelling[quiz_index]

    for i in range(len(numb_spelling)):
        le = getattr(ui, f"numb3_le_{i}")
        le.setText(numb_spelling[i])

    quiz_le = getattr(ui, f"numb3_le_{str(quiz_index)}")
    quiz_le.setText("")
    quiz_le.setStyleSheet(QUIZ_LE_STYLE)
    quiz_le.setReadOnly(False)
    quiz_le.setFocus()


def check_answer(ui, alphabet):
    if alphabet == "":
        return
    elif alphabet == quiz:
        quiz_le = getattr(ui, f"numb3_le_{str(quiz_index)}")
        quiz_le.setReadOnly(True)
        ui.messages.setText("참 잘했어요!!")
        main.delay_time(ui, 100)
        utils.playWOW()
        main.delay_time(ui, 3000)
        utils.play_MP3(f"resources/numb2/eng/eng_{currentNumber}.mp3")
        main.delay_time(ui, 2000)
        current_number = int(ui.numb3_numb.text())
        if current_number < 20:
            next_number = current_number + 1
        else:
            next_number = 0
        new_game(ui, next_number)


def keyb(ui, key):
    quiz_le = getattr(ui, f"numb3_le_{str(quiz_index)}")
    quiz_le.setFocus()
    utils.press_key(ui, key)
