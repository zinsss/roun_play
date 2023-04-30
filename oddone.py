import random
import main, utils, symbols

DEFAULT_STYLE_0 = """
color: rgb(100, 150, 125);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-right:none;
border-top-left-radius:50px;
border-bottom-left-radius:50px;
"""
DEFAULT_STYLE_123 = """
color: rgb(100, 150, 125);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-right:none;
"""
DEFAULT_STYLE_4 = """
color: rgb(100, 150, 125);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-top-right-radius:50px;
border-bottom-right-radius:50px;
"""
ANSWER_STYLE_0 = """
color: rgb(150, 100, 75);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-right:none;
border-top-left-radius:50px;
border-bottom-left-radius:50px;
"""
ANSWER_STYLE_123 = """
color: rgb(150, 100, 75);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-right:none;
"""
ANSWER_STYLE_4 = """
color: rgb(150, 100, 75);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-top-right-radius:50px;
border-bottom-right-radius:50px;
"""
WRONG_STYLE_0 = """
color: rgb(144, 166, 155);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-right:none;
border-top-left-radius:50px;
border-bottom-left-radius:50px;
"""
WRONG_STYLE_123 = """
color: rgb(144, 166, 155);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-right:none;
"""
WRONG_STYLE_4 = """
color: rgb(144, 166, 155);
background-color: rgb(160, 175, 150);
border:1px solid rgb(125,150,100);
border-top-right-radius:50px;
border-bottom-right-radius:50px;
"""
STYLE_0 = [DEFAULT_STYLE_0, ANSWER_STYLE_0, WRONG_STYLE_0]
STYLE_123 = [DEFAULT_STYLE_123, ANSWER_STYLE_123, WRONG_STYLE_123]
STYLE_4 = [DEFAULT_STYLE_4, ANSWER_STYLE_4, WRONG_STYLE_4]

quiz_1 = ""
quiz_2 = ""
quiz_3 = ""

quiz_1_done = False
quiz_2_done = False
quiz_3_done = False


def initiate(ui):
    global quiz_1, quiz_2, quiz_3, quiz_1_done, quiz_2_done, quiz_3_done
    for i in range(1, 4):
        globals()[f"quiz_{i}_done"] = False
        quiz_index = random.randint(0, 4)
        selected = random.sample(symbols.SYMB_LIST, 2)
        examples = random.sample(selected[0], 4)
        odd_one = random.choice(selected[1])
        examples.insert(quiz_index, odd_one)
        globals()[f"quiz_{i}"] = odd_one
        for x in range(0, 5):
            btn = getattr(ui, f"odd{i}_{x}")
            btn.setText(examples[x])
            if x == 0:
                btn.setStyleSheet(DEFAULT_STYLE_0)
            elif x == 4:
                btn.setStyleSheet(DEFAULT_STYLE_4)
            else:
                btn.setStyleSheet(DEFAULT_STYLE_123)


def check_answer(ui, quiz: int, btn_no: int):
    if btn_no == 0:
        stylesheet = STYLE_0
    elif btn_no == 4:
        stylesheet = STYLE_4
    else:
        stylesheet = STYLE_123

    btn_pressed = getattr(ui, f"odd{quiz}_{btn_no}")
    symb = btn_pressed.text()

    target_quiz = globals()[f"quiz_{quiz}"]
    if target_quiz == symb:
        for i in range(0, 5):
            btn = getattr(ui, f"odd{quiz}_{i}")
            if btn.text() == symb:
                if i == 0:
                    btn.setStyleSheet(ANSWER_STYLE_0)
                elif i == 4:
                    btn.setStyleSheet(ANSWER_STYLE_4)
                else:
                    btn.setStyleSheet(ANSWER_STYLE_123)
            else:
                if i == 0:
                    btn.setStyleSheet(WRONG_STYLE_0)
                elif i == 4:
                    btn.setStyleSheet(WRONG_STYLE_4)
                else:
                    btn.setStyleSheet(WRONG_STYLE_123)
        utils.playWOW()
        globals()[f"quiz_{quiz}_done"] = True
    else:
        btn = getattr(ui, f"odd{quiz}_{btn_no}")
        btn.setStyleSheet(stylesheet[2])

    main.delay_time(ui, 1500)

    if quiz_1_done and quiz_2_done and quiz_3_done:
        utils.play_tts("참 잘했어요~", kr=True)
        initiate(ui)
