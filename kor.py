import random
from PySide6.QtGui import QPixmap
import main, utils

EXAMPLES = {
    "be_quiet.png": ["조용히하세요.", "쉿~!", "시끄러워요."],
    "brush_teeth.png": ["양치해요.", "이를 닦아요.", "치카치카해요."],
    "clean_up.png": ["청소해요.", "정리해요."],
    "hello.png": ["안녕하세요.", "인사해요.", "안녕히계세요."],
    "help.png": ["도와주세요.", "도와줄께요."],
    "hungry.png": ["배고파요.", "밥 주세요.", "밥 먹고 싶어요.", "밥 먹어요."],
    "love.png": ["사랑해요."],
    "need_to_pee.png": ["쉬 하고 싶어요.", "쉬 마려워요", "오줌 싸고 싶어요."],
    "need_to_poop.png": ["응가 하고 싶어요.", "똥 마려워요.", "똥 싸고 싶어요."],
    "sit_down.png": ["앉아요.", "자리에 앉아요.", "앉아보세요."],
    "thank_you.png": ["고마워.", "감사합니다.", "고마워요."],
    "thirsty.png": ["목 말라요.", "물 마시고 싶어요.", "물 주세요."],
    "where_is_it.png": ["어디에 있어요?", "어디있지?", "찾아주세요."],
}

IMAGE_FILES = list(EXAMPLES.keys())

DEFAULT_STYLE = """
background-color: rgb(130, 160, 160);
border:1px solid rgb(120, 150, 150);
border-radius:30px;
color: rgb(33, 99, 99);
"""

WRONG_STYLE = """
background-color: rgb(130, 160, 160);
border:1px solid rgb(120, 150, 150);
border-radius:30px;
color: rgb(180, 80, 80);
"""

ANSWER_STYLE = """
background-color: rgb(130, 160, 160);
border:1px solid rgb(120, 150, 150);
border-radius:30px;
color: rgb(50, 125, 225);
"""

quiz_index = 0


def new_game(ui):
    global quiz_index
    quiz_index = random.randint(0, 4)

    imgFile = random.choice(IMAGE_FILES)

    temp = random.sample(IMAGE_FILES, 4)
    while imgFile in temp:
        temp = random.sample(IMAGE_FILES, 4)

    temp.insert(quiz_index, imgFile)

    ui.kor_img.setPixmap(QPixmap(f"resources/kor/{imgFile}"))

    for i in range(0, 5):
        btn = getattr(ui, f"kor_ans_{i}")
        textz = random.choice(EXAMPLES[temp[i]])
        btn.setStyleSheet(DEFAULT_STYLE)
        btn.setText(textz)


def check_answer(ui, btn_index: int):
    if btn_index == quiz_index:
        for i in range(0, 5):
            btn = getattr(ui, f"kor_ans_{i}")
            if i == quiz_index:
                btn.setStyleSheet(ANSWER_STYLE)
                btn_text = btn.text()
            else:
                btn.setStyleSheet(WRONG_STYLE)
            ui.messages.setText("참 잘했어요!!")
        main.delay_time(ui, 100)
        utils.playWOW()
        main.delay_time(ui, 3000)
        utils.play_tts(btn_text, kr=True)
        main.delay_time(ui, 3000)
        new_game(ui)
    else:
        btn = getattr(ui, f"kor_ans_{btn_index}")
        btn.setStyleSheet(WRONG_STYLE)
