from PySide6.QtGui import QColor, QTextCursor, QPixmap
from PySide6.QtCore import Qt
import main, utils


RED = [(180, 80, 80), "Red", "빨간색", "red.png"]
ORANGE = [(200, 120, 90), "Orange", "주황색", "orange.png"]
PEACH = [(188, 133, 111), "Peach", "살구색", "peach.png"]
BEIGE = [(180, 180, 150), "Beige", "베이지색", "beige.png"]
YELLOW = [(190, 170, 100), "Yellow", "노란색", "yellow.png"]
YGREEN = [(100, 155, 88), "Yellow Green", "연두색", "ygreen.png"]
GREEN = [(55, 144, 88), "Green", "녹색, 초록색", "green.png"]
TEAL = [(75, 150, 150), "Teal", "청록색", "teal.png"]
SBLUE = [(125, 175, 200), "Sky Blue", "하늘색", "sblue.png"]
BLUE = [(75, 120, 175), "Blue", "파란색", "blue.png"]
NBLUE = [(60, 80, 120), "Navy Blue", "남색", "nblue.png"]
VIOLET = [(100, 90, 150), "Violet", "청자색", "violet.png"]
PURPLE = [(140, 90, 150), "Purple", "보라색", "purple.png"]
PINK = [(180, 120, 140), "Pink", "핑크색, 분홍색", "pink.png"]
BROWN = [(125, 100, 80), "Brown", "갈색", "brown.png"]
WHITE = [(230, 230, 230), "White", "흰색, 하얀색", "white.png"]
GRAY = [(120, 120, 120), "Gray", "회색", "gray.png"]
BLACK = [(20, 20, 20), "Black", "검정색, 검은색", "black.png"]


def initiate(ui):
    ui.color_trains.setText("")
    ui.color_name_eng.setText("")
    ui.color_name_kor.setText("")
    ui.color_img.clear()
    ui.color_trains.setCursorWidth(0)
    ui.color_trains.setAlignment(Qt.AlignRight)


def add_train(ui, color):
    train_text = ui.color_trains.toPlainText()
    text_count = len(train_text)
    if text_count >= 18:
        initiate(ui)
    alphab = "a" if text_count == 0 or text_count >= 18 else "c"
    ui.color_trains.setFocus()
    ui.color_trains.moveCursor(QTextCursor.End)
    ui.color_trains.setTextColor(QColor(*color[0]))
    utils.press_key(ui, alphab)
    ui.color_name_eng.setStyleSheet(f"color:rgb{str(color[0])};")
    ui.color_name_eng.setText(color[1])
    ui.color_name_kor.setStyleSheet(f"color:rgb{str(color[0])};")
    ui.color_name_kor.setText(color[2])
    ui.color_img.setPixmap(QPixmap("resources/colors/" + color[3]))
    utils.play_tts(color[1])
    main.delay_time(ui, 800)
    utils.play_tts(color[2], kr=True)
    main.delay_time(ui, 1500)


def backspace(ui):
    ui.color_name_eng.setText("")
    ui.color_name_kor.setText("")
    ui.color_img.clear()
    ui.color_trains.setFocus()
    ui.color_trains.moveCursor(QTextCursor.End)
    utils.press_key(ui, "backspace")
