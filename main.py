import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice, QEventLoop, QTimer
import pyautogui as pag

import utils, numb1, numb2, numb3, eng1, eng2, opposites
import kor, colors, oddone, patterns, directions, oxquiz


def loadUi():
    loader = QUiLoader()
    ui_file = QFile("main.ui")
    ui_file.open(QFile.ReadOnly)
    ui = loader.load(ui_file)
    ui_file.close()
    return ui


def menu_navigation(ui, index_no):
    app_titles = [
        "숫자놀이 #1",
        "숫자놀이 #2",
        "숫자놀이 #3",
        "영어놀이 #1",
        "영어놀이 #2",
        "반대말 놀이",
        "한글놀이",
        "색깔놀이",
        "다른 것 찾기",
        "순서 찾기",
        "위치 찾기",
        "OX 퀴즈",
    ]

    app_messages = [
        "빈칸에 들어갈 숫자를 입력하세요.",
        "제일 좋아하는 숫자를 눌러보세요.",
        "1-20까지 영어 스펠링을 맞춰보세요.",
        "Phonics !!!",
        "단어의 그림을 찾아보세요~",
        "반대말을 영어/우리말로 배워보자!",
        "그림의 상황에서 뭐라고 말해야할까요?",
        "로운이가 좋아하는 색깔을 눌러보세요~",
        "다른것을 찾아보자~ 로운이 화이팅!",
        "물음표에 들어갈 모양은 뭘까요??",
        "질문을 읽고 맞는 그림을 찾아보세요~",
        "맞는말인가요? 틀린말인가요?",
    ]

    ui.stackMain.setCurrentIndex(1)
    ui.stackApps.setCurrentIndex(index_no)
    ui.app_name.setText(app_titles[index_no])
    ui.messages.setText(app_messages[index_no])


def delay_time(ui, mmsec):
    loop = QEventLoop()  # equivalent to sleep in pyqt5
    QTimer.singleShot(mmsec, loop.quit)  # equivalent to sleep in pyqt5
    loop.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = loadUi()

    ########################################################################################

    # Always Start at Home
    ui.stackMain.setCurrentIndex(0)

    # Activate All Plays
    numb1.new_game(ui)
    numb3.new_game(ui, 0)
    eng1.new_game(ui)
    eng2.new_game(ui)
    opposites.initiate(ui)
    kor.new_game(ui)
    colors.initiate(ui)
    oddone.initiate(ui)
    patterns.initiate(ui)

    # Home Menus
    ui.numb1_btn.clicked.connect(lambda: menu_navigation(ui, 0))
    ui.numb2_btn.clicked.connect(lambda: menu_navigation(ui, 1))
    ui.numb3_btn.clicked.connect(lambda: menu_navigation(ui, 2))
    ui.eng1_btn.clicked.connect(lambda: menu_navigation(ui, 3))
    ui.eng2_btn.clicked.connect(lambda: menu_navigation(ui, 4))
    ui.opposites_btn.clicked.connect(lambda: menu_navigation(ui, 5))
    ui.kor_btn.clicked.connect(lambda: menu_navigation(ui, 6))
    ui.colors_btn.clicked.connect(lambda: menu_navigation(ui, 7))
    ui.oddone_btn.clicked.connect(lambda: menu_navigation(ui, 8))
    ui.patterns_btn.clicked.connect(lambda: menu_navigation(ui, 9))
    ui.directions_btn.clicked.connect(lambda: menu_navigation(ui, 10))
    ui.oxquiz_btn.clicked.connect(lambda: menu_navigation(ui, 11))

    # StackApps Menus
    ui.numb1_menuBtn.clicked.connect(lambda: menu_navigation(ui, 0))
    ui.numb2_menuBtn.clicked.connect(lambda: menu_navigation(ui, 1))
    ui.numb3_menuBtn.clicked.connect(lambda: menu_navigation(ui, 2))
    ui.eng1_menuBtn.clicked.connect(lambda: menu_navigation(ui, 3))
    ui.eng2_menuBtn.clicked.connect(lambda: menu_navigation(ui, 4))
    ui.opposites_menuBtn.clicked.connect(lambda: menu_navigation(ui, 5))
    ui.kor_menuBtn.clicked.connect(lambda: menu_navigation(ui, 6))
    ui.colors_menuBtn.clicked.connect(lambda: menu_navigation(ui, 7))
    ui.oddone_menuBtn.clicked.connect(lambda: menu_navigation(ui, 8))
    ui.patterns_menuBtn.clicked.connect(lambda: menu_navigation(ui, 9))
    ui.directions_menuBtn.clicked.connect(lambda: menu_navigation(ui, 10))
    ui.oxquiz_menuBtn.clicked.connect(lambda: menu_navigation(ui, 11))

    # NumberPlay 1
    ui.numb1_0.textEdited.connect(lambda: numb1.check_answer(ui, ui.numb1_0.text()))
    ui.numb1_1.textEdited.connect(lambda: numb1.check_answer(ui, ui.numb1_1.text()))
    ui.numb1_2.textEdited.connect(lambda: numb1.check_answer(ui, ui.numb1_2.text()))
    ui.numb1_3.textEdited.connect(lambda: numb1.check_answer(ui, ui.numb1_3.text()))
    ui.numb1_4.textEdited.connect(lambda: numb1.check_answer(ui, ui.numb1_4.text()))
    ui.n1_new_btn.clicked.connect(lambda: numb1.new_game(ui))
    ui.n1_clr_btn.clicked.connect(lambda: numb1.clear_quiz(ui))
    ui.n1_bs_btn.clicked.connect(lambda: numb1.keyb(ui, "backspace"))
    ui.n1_0_btn.clicked.connect(lambda: numb1.keyb(ui, "0"))
    ui.n1_1_btn.clicked.connect(lambda: numb1.keyb(ui, "1"))
    ui.n1_2_btn.clicked.connect(lambda: numb1.keyb(ui, "2"))
    ui.n1_3_btn.clicked.connect(lambda: numb1.keyb(ui, "3"))
    ui.n1_4_btn.clicked.connect(lambda: numb1.keyb(ui, "4"))
    ui.n1_5_btn.clicked.connect(lambda: numb1.keyb(ui, "5"))
    ui.n1_6_btn.clicked.connect(lambda: numb1.keyb(ui, "6"))
    ui.n1_7_btn.clicked.connect(lambda: numb1.keyb(ui, "7"))
    ui.n1_8_btn.clicked.connect(lambda: numb1.keyb(ui, "8"))
    ui.n1_9_btn.clicked.connect(lambda: numb1.keyb(ui, "9"))

    # NumberPlay 2
    ui.numb2_0.clicked.connect(lambda: numb2.numb_select(ui, 0))
    ui.numb2_1.clicked.connect(lambda: numb2.numb_select(ui, 1))
    ui.numb2_2.clicked.connect(lambda: numb2.numb_select(ui, 2))
    ui.numb2_3.clicked.connect(lambda: numb2.numb_select(ui, 3))
    ui.numb2_4.clicked.connect(lambda: numb2.numb_select(ui, 4))
    ui.numb2_5.clicked.connect(lambda: numb2.numb_select(ui, 5))
    ui.numb2_6.clicked.connect(lambda: numb2.numb_select(ui, 6))
    ui.numb2_7.clicked.connect(lambda: numb2.numb_select(ui, 7))
    ui.numb2_8.clicked.connect(lambda: numb2.numb_select(ui, 8))
    ui.numb2_9.clicked.connect(lambda: numb2.numb_select(ui, 9))
    ui.numb2_10.clicked.connect(lambda: numb2.numb_select(ui, 10))
    ui.numb2_11.clicked.connect(lambda: numb2.numb_select(ui, 11))
    ui.numb2_12.clicked.connect(lambda: numb2.numb_select(ui, 12))
    ui.numb2_13.clicked.connect(lambda: numb2.numb_select(ui, 13))
    ui.numb2_14.clicked.connect(lambda: numb2.numb_select(ui, 14))
    ui.numb2_15.clicked.connect(lambda: numb2.numb_select(ui, 15))
    ui.numb2_16.clicked.connect(lambda: numb2.numb_select(ui, 16))
    ui.numb2_17.clicked.connect(lambda: numb2.numb_select(ui, 17))
    ui.numb2_18.clicked.connect(lambda: numb2.numb_select(ui, 18))
    ui.numb2_19.clicked.connect(lambda: numb2.numb_select(ui, 19))
    ui.numb2_20.clicked.connect(lambda: numb2.numb_select(ui, 20))
    ui.numb2_21.clicked.connect(lambda: numb2.numb_select(ui, 21))
    ui.numb2_22.clicked.connect(lambda: numb2.numb_select(ui, 22))
    ui.numb2_23.clicked.connect(lambda: numb2.numb_select(ui, 23))
    ui.numb2_24.clicked.connect(lambda: numb2.numb_select(ui, 24))
    ui.numb2_25.clicked.connect(lambda: numb2.numb_select(ui, 25))
    ui.numb2_26.clicked.connect(lambda: numb2.numb_select(ui, 26))
    ui.numb2_27.clicked.connect(lambda: numb2.numb_select(ui, 27))
    ui.numb2_28.clicked.connect(lambda: numb2.numb_select(ui, 28))
    ui.numb2_29.clicked.connect(lambda: numb2.numb_select(ui, 29))
    ui.numb2_30.clicked.connect(lambda: numb2.numb_select(ui, 30))
    ui.numb2_31.clicked.connect(lambda: numb2.numb_select(ui, 31))
    ui.numb2_32.clicked.connect(lambda: numb2.numb_select(ui, 32))
    ui.numb2_33.clicked.connect(lambda: numb2.numb_select(ui, 33))
    ui.numb2_34.clicked.connect(lambda: numb2.numb_select(ui, 34))
    ui.numb2_35.clicked.connect(lambda: numb2.numb_select(ui, 35))
    ui.numb2_36.clicked.connect(lambda: numb2.numb_select(ui, 36))
    ui.numb2_37.clicked.connect(lambda: numb2.numb_select(ui, 37))
    ui.numb2_38.clicked.connect(lambda: numb2.numb_select(ui, 38))
    ui.numb2_39.clicked.connect(lambda: numb2.numb_select(ui, 39))
    ui.numb2_40.clicked.connect(lambda: numb2.numb_select(ui, 40))
    ui.numb2_41.clicked.connect(lambda: numb2.numb_select(ui, 41))
    ui.numb2_42.clicked.connect(lambda: numb2.numb_select(ui, 42))
    ui.numb2_43.clicked.connect(lambda: numb2.numb_select(ui, 43))
    ui.numb2_44.clicked.connect(lambda: numb2.numb_select(ui, 44))
    ui.numb2_45.clicked.connect(lambda: numb2.numb_select(ui, 45))
    ui.numb2_46.clicked.connect(lambda: numb2.numb_select(ui, 46))
    ui.numb2_47.clicked.connect(lambda: numb2.numb_select(ui, 47))
    ui.numb2_48.clicked.connect(lambda: numb2.numb_select(ui, 48))
    ui.numb2_49.clicked.connect(lambda: numb2.numb_select(ui, 49))
    ui.numb2_50.clicked.connect(lambda: numb2.numb_select(ui, 50))
    ui.numb2_51.clicked.connect(lambda: numb2.numb_select(ui, 51))
    ui.numb2_52.clicked.connect(lambda: numb2.numb_select(ui, 52))
    ui.numb2_53.clicked.connect(lambda: numb2.numb_select(ui, 53))
    ui.numb2_54.clicked.connect(lambda: numb2.numb_select(ui, 54))
    ui.numb2_55.clicked.connect(lambda: numb2.numb_select(ui, 55))
    ui.numb2_56.clicked.connect(lambda: numb2.numb_select(ui, 56))
    ui.numb2_57.clicked.connect(lambda: numb2.numb_select(ui, 57))
    ui.numb2_58.clicked.connect(lambda: numb2.numb_select(ui, 58))
    ui.numb2_59.clicked.connect(lambda: numb2.numb_select(ui, 59))
    ui.numb2_60.clicked.connect(lambda: numb2.numb_select(ui, 60))
    ui.numb2_61.clicked.connect(lambda: numb2.numb_select(ui, 61))
    ui.numb2_62.clicked.connect(lambda: numb2.numb_select(ui, 62))
    ui.numb2_63.clicked.connect(lambda: numb2.numb_select(ui, 63))
    ui.numb2_64.clicked.connect(lambda: numb2.numb_select(ui, 64))
    ui.numb2_65.clicked.connect(lambda: numb2.numb_select(ui, 65))
    ui.numb2_66.clicked.connect(lambda: numb2.numb_select(ui, 66))
    ui.numb2_67.clicked.connect(lambda: numb2.numb_select(ui, 67))
    ui.numb2_68.clicked.connect(lambda: numb2.numb_select(ui, 68))
    ui.numb2_69.clicked.connect(lambda: numb2.numb_select(ui, 69))
    ui.numb2_70.clicked.connect(lambda: numb2.numb_select(ui, 70))
    ui.numb2_71.clicked.connect(lambda: numb2.numb_select(ui, 71))
    ui.numb2_72.clicked.connect(lambda: numb2.numb_select(ui, 72))
    ui.numb2_73.clicked.connect(lambda: numb2.numb_select(ui, 73))
    ui.numb2_74.clicked.connect(lambda: numb2.numb_select(ui, 74))
    ui.numb2_75.clicked.connect(lambda: numb2.numb_select(ui, 75))
    ui.numb2_76.clicked.connect(lambda: numb2.numb_select(ui, 76))
    ui.numb2_77.clicked.connect(lambda: numb2.numb_select(ui, 77))
    ui.numb2_78.clicked.connect(lambda: numb2.numb_select(ui, 78))
    ui.numb2_79.clicked.connect(lambda: numb2.numb_select(ui, 79))
    ui.numb2_80.clicked.connect(lambda: numb2.numb_select(ui, 80))
    ui.numb2_81.clicked.connect(lambda: numb2.numb_select(ui, 81))
    ui.numb2_82.clicked.connect(lambda: numb2.numb_select(ui, 82))
    ui.numb2_83.clicked.connect(lambda: numb2.numb_select(ui, 83))
    ui.numb2_84.clicked.connect(lambda: numb2.numb_select(ui, 84))
    ui.numb2_85.clicked.connect(lambda: numb2.numb_select(ui, 85))
    ui.numb2_86.clicked.connect(lambda: numb2.numb_select(ui, 86))
    ui.numb2_87.clicked.connect(lambda: numb2.numb_select(ui, 87))
    ui.numb2_88.clicked.connect(lambda: numb2.numb_select(ui, 88))
    ui.numb2_89.clicked.connect(lambda: numb2.numb_select(ui, 89))
    ui.numb2_90.clicked.connect(lambda: numb2.numb_select(ui, 90))
    ui.numb2_91.clicked.connect(lambda: numb2.numb_select(ui, 91))
    ui.numb2_92.clicked.connect(lambda: numb2.numb_select(ui, 92))
    ui.numb2_93.clicked.connect(lambda: numb2.numb_select(ui, 93))
    ui.numb2_94.clicked.connect(lambda: numb2.numb_select(ui, 94))
    ui.numb2_95.clicked.connect(lambda: numb2.numb_select(ui, 95))
    ui.numb2_96.clicked.connect(lambda: numb2.numb_select(ui, 96))
    ui.numb2_97.clicked.connect(lambda: numb2.numb_select(ui, 97))
    ui.numb2_98.clicked.connect(lambda: numb2.numb_select(ui, 98))
    ui.numb2_99.clicked.connect(lambda: numb2.numb_select(ui, 99))
    ui.numb2_100.clicked.connect(lambda: numb2.numb_select(ui, 100))
    ui.numb2_kor.clicked.connect(lambda: numb2.play_mp3(ui, "kor"))
    ui.numb2_eng.clicked.connect(lambda: numb2.play_mp3(ui, "eng"))

    # NumberPlay 3
    ui.numb3_no_0.clicked.connect(lambda: numb3.new_game(ui, 0))
    ui.numb3_no_1.clicked.connect(lambda: numb3.new_game(ui, 1))
    ui.numb3_no_2.clicked.connect(lambda: numb3.new_game(ui, 2))
    ui.numb3_no_3.clicked.connect(lambda: numb3.new_game(ui, 3))
    ui.numb3_no_4.clicked.connect(lambda: numb3.new_game(ui, 4))
    ui.numb3_no_5.clicked.connect(lambda: numb3.new_game(ui, 5))
    ui.numb3_no_6.clicked.connect(lambda: numb3.new_game(ui, 6))
    ui.numb3_no_7.clicked.connect(lambda: numb3.new_game(ui, 7))
    ui.numb3_no_8.clicked.connect(lambda: numb3.new_game(ui, 8))
    ui.numb3_no_9.clicked.connect(lambda: numb3.new_game(ui, 9))
    ui.numb3_no_10.clicked.connect(lambda: numb3.new_game(ui, 10))
    ui.numb3_no_11.clicked.connect(lambda: numb3.new_game(ui, 11))
    ui.numb3_no_12.clicked.connect(lambda: numb3.new_game(ui, 12))
    ui.numb3_no_13.clicked.connect(lambda: numb3.new_game(ui, 13))
    ui.numb3_no_14.clicked.connect(lambda: numb3.new_game(ui, 14))
    ui.numb3_no_15.clicked.connect(lambda: numb3.new_game(ui, 15))
    ui.numb3_no_16.clicked.connect(lambda: numb3.new_game(ui, 16))
    ui.numb3_no_17.clicked.connect(lambda: numb3.new_game(ui, 17))
    ui.numb3_no_18.clicked.connect(lambda: numb3.new_game(ui, 18))
    ui.numb3_no_19.clicked.connect(lambda: numb3.new_game(ui, 19))
    ui.numb3_no_20.clicked.connect(lambda: numb3.new_game(ui, 20))
    ui.numb3_le_0.textEdited.connect(
        lambda: numb3.check_answer(ui, ui.numb3_le_0.text())
    )
    ui.numb3_le_1.textEdited.connect(
        lambda: numb3.check_answer(ui, ui.numb3_le_1.text())
    )
    ui.numb3_le_2.textEdited.connect(
        lambda: numb3.check_answer(ui, ui.numb3_le_2.text())
    )
    ui.numb3_le_3.textEdited.connect(
        lambda: numb3.check_answer(ui, ui.numb3_le_3.text())
    )
    ui.numb3_le_4.textEdited.connect(
        lambda: numb3.check_answer(ui, ui.numb3_le_4.text())
    )
    ui.numb3_le_5.textEdited.connect(
        lambda: numb3.check_answer(ui, ui.numb3_le_5.text())
    )
    ui.numb3_le_6.textEdited.connect(
        lambda: numb3.check_answer(ui, ui.numb3_le_6.text())
    )
    ui.numb3_le_7.textEdited.connect(
        lambda: numb3.check_answer(ui, ui.numb3_le_7.text())
    )
    ui.numb3_le_8.textEdited.connect(
        lambda: numb3.check_answer(ui, ui.numb3_le_8.text())
    )
    ui.numb3_1.clicked.connect(lambda: numb3.keyb(ui, "1"))
    ui.numb3_2.clicked.connect(lambda: numb3.keyb(ui, "2"))
    ui.numb3_3.clicked.connect(lambda: numb3.keyb(ui, "3"))
    ui.numb3_4.clicked.connect(lambda: numb3.keyb(ui, "4"))
    ui.numb3_5.clicked.connect(lambda: numb3.keyb(ui, "5"))
    ui.numb3_6.clicked.connect(lambda: numb3.keyb(ui, "6"))
    ui.numb3_7.clicked.connect(lambda: numb3.keyb(ui, "7"))
    ui.numb3_8.clicked.connect(lambda: numb3.keyb(ui, "8"))
    ui.numb3_9.clicked.connect(lambda: numb3.keyb(ui, "9"))
    ui.numb3_0.clicked.connect(lambda: numb3.keyb(ui, "0"))
    ui.numb3_bs.clicked.connect(lambda: numb3.keyb(ui, "backspace"))
    ui.numb3_q.clicked.connect(lambda: numb3.keyb(ui, "q"))
    ui.numb3_w.clicked.connect(lambda: numb3.keyb(ui, "w"))
    ui.numb3_e.clicked.connect(lambda: numb3.keyb(ui, "e"))
    ui.numb3_r.clicked.connect(lambda: numb3.keyb(ui, "r"))
    ui.numb3_t.clicked.connect(lambda: numb3.keyb(ui, "t"))
    ui.numb3_y.clicked.connect(lambda: numb3.keyb(ui, "y"))
    ui.numb3_u.clicked.connect(lambda: numb3.keyb(ui, "u"))
    ui.numb3_i.clicked.connect(lambda: numb3.keyb(ui, "i"))
    ui.numb3_o.clicked.connect(lambda: numb3.keyb(ui, "o"))
    ui.numb3_p.clicked.connect(lambda: numb3.keyb(ui, "p"))
    ui.numb3_a.clicked.connect(lambda: numb3.keyb(ui, "a"))
    ui.numb3_s.clicked.connect(lambda: numb3.keyb(ui, "s"))
    ui.numb3_d.clicked.connect(lambda: numb3.keyb(ui, "d"))
    ui.numb3_f.clicked.connect(lambda: numb3.keyb(ui, "f"))
    ui.numb3_g.clicked.connect(lambda: numb3.keyb(ui, "g"))
    ui.numb3_h.clicked.connect(lambda: numb3.keyb(ui, "h"))
    ui.numb3_j.clicked.connect(lambda: numb3.keyb(ui, "j"))
    ui.numb3_k.clicked.connect(lambda: numb3.keyb(ui, "k"))
    ui.numb3_l.clicked.connect(lambda: numb3.keyb(ui, "l"))
    ui.numb3_z.clicked.connect(lambda: numb3.keyb(ui, "z"))
    ui.numb3_x.clicked.connect(lambda: numb3.keyb(ui, "x"))
    ui.numb3_c.clicked.connect(lambda: numb3.keyb(ui, "c"))
    ui.numb3_v.clicked.connect(lambda: numb3.keyb(ui, "v"))
    ui.numb3_b.clicked.connect(lambda: numb3.keyb(ui, "b"))
    ui.numb3_n.clicked.connect(lambda: numb3.keyb(ui, "n"))
    ui.numb3_m.clicked.connect(lambda: numb3.keyb(ui, "m"))

    # EnglishPlay 1
    ui.eng1_alphabet.textEdited.connect(
        lambda: eng1.load_phonics(ui, ui.eng1_alphabet.text())
    )
    ui.eng1_spell_0.textEdited.connect(
        lambda: eng1.check_answer(ui, ui.eng1_spell_0.text())
    )
    ui.eng1_spell_1.textEdited.connect(
        lambda: eng1.check_answer(ui, ui.eng1_spell_1.text())
    )
    ui.eng1_spell_2.textEdited.connect(
        lambda: eng1.check_answer(ui, ui.eng1_spell_2.text())
    )
    ui.eng1_spell_3.textEdited.connect(
        lambda: eng1.check_answer(ui, ui.eng1_spell_3.text())
    )
    ui.eng1_spell_4.textEdited.connect(
        lambda: eng1.check_answer(ui, ui.eng1_spell_4.text())
    )
    ui.eng1_spell_5.textEdited.connect(
        lambda: eng1.check_answer(ui, ui.eng1_spell_5.text())
    )
    ui.eng1_spell_6.textEdited.connect(
        lambda: eng1.check_answer(ui, ui.eng1_spell_6.text())
    )
    ui.eng1_spell_7.textEdited.connect(
        lambda: eng1.check_answer(ui, ui.eng1_spell_7.text())
    )
    ui.eng1_spell_8.textEdited.connect(
        lambda: eng1.check_answer(ui, ui.eng1_spell_8.text())
    )
    ui.eng1_1.clicked.connect(lambda: eng1.keyb(ui, "1"))
    ui.eng1_2.clicked.connect(lambda: eng1.keyb(ui, "2"))
    ui.eng1_3.clicked.connect(lambda: eng1.keyb(ui, "3"))
    ui.eng1_4.clicked.connect(lambda: eng1.keyb(ui, "4"))
    ui.eng1_5.clicked.connect(lambda: eng1.keyb(ui, "5"))
    ui.eng1_6.clicked.connect(lambda: eng1.keyb(ui, "6"))
    ui.eng1_7.clicked.connect(lambda: eng1.keyb(ui, "7"))
    ui.eng1_8.clicked.connect(lambda: eng1.keyb(ui, "8"))
    ui.eng1_9.clicked.connect(lambda: eng1.keyb(ui, "9"))
    ui.eng1_0.clicked.connect(lambda: eng1.keyb(ui, "0"))
    ui.eng1_bs.clicked.connect(lambda: eng1.keyb(ui, "backspace"))
    ui.eng1_q.clicked.connect(lambda: eng1.keyb(ui, "q"))
    ui.eng1_w.clicked.connect(lambda: eng1.keyb(ui, "w"))
    ui.eng1_e.clicked.connect(lambda: eng1.keyb(ui, "e"))
    ui.eng1_r.clicked.connect(lambda: eng1.keyb(ui, "r"))
    ui.eng1_t.clicked.connect(lambda: eng1.keyb(ui, "t"))
    ui.eng1_y.clicked.connect(lambda: eng1.keyb(ui, "y"))
    ui.eng1_u.clicked.connect(lambda: eng1.keyb(ui, "u"))
    ui.eng1_i.clicked.connect(lambda: eng1.keyb(ui, "i"))
    ui.eng1_o.clicked.connect(lambda: eng1.keyb(ui, "o"))
    ui.eng1_p.clicked.connect(lambda: eng1.keyb(ui, "p"))
    ui.eng1_a.clicked.connect(lambda: eng1.keyb(ui, "a"))
    ui.eng1_s.clicked.connect(lambda: eng1.keyb(ui, "s"))
    ui.eng1_d.clicked.connect(lambda: eng1.keyb(ui, "d"))
    ui.eng1_f.clicked.connect(lambda: eng1.keyb(ui, "f"))
    ui.eng1_g.clicked.connect(lambda: eng1.keyb(ui, "g"))
    ui.eng1_h.clicked.connect(lambda: eng1.keyb(ui, "h"))
    ui.eng1_j.clicked.connect(lambda: eng1.keyb(ui, "j"))
    ui.eng1_k.clicked.connect(lambda: eng1.keyb(ui, "k"))
    ui.eng1_l.clicked.connect(lambda: eng1.keyb(ui, "l"))
    ui.eng1_z.clicked.connect(lambda: eng1.keyb(ui, "z"))
    ui.eng1_x.clicked.connect(lambda: eng1.keyb(ui, "x"))
    ui.eng1_c.clicked.connect(lambda: eng1.keyb(ui, "c"))
    ui.eng1_v.clicked.connect(lambda: eng1.keyb(ui, "v"))
    ui.eng1_b.clicked.connect(lambda: eng1.keyb(ui, "b"))
    ui.eng1_n.clicked.connect(lambda: eng1.keyb(ui, "n"))
    ui.eng1_m.clicked.connect(lambda: eng1.keyb(ui, "m"))

    # EglishPlay 2
    ui.eng2_ans0.clicked.connect(lambda: eng2.check_answer(ui, 0))
    ui.eng2_ans1.clicked.connect(lambda: eng2.check_answer(ui, 1))
    ui.eng2_ans2.clicked.connect(lambda: eng2.check_answer(ui, 2))
    ui.eng2_ans3.clicked.connect(lambda: eng2.check_answer(ui, 3))
    ui.eng2_ans4.clicked.connect(lambda: eng2.check_answer(ui, 4))

    # Opposites
    ui.opp_combo.currentIndexChanged.connect(lambda: opposites.combo_select(ui))
    ui.opp_prev.clicked.connect(lambda: opposites.prev(ui))
    ui.opp_next.clicked.connect(lambda: opposites.next(ui))
    ui.opp_eng_btn.clicked.connect(lambda: opposites.playmp3(ui))
    ui.opp_kor_btn.clicked.connect(lambda: opposites.playmp3(ui, kor=True))

    # KoreanPlay
    ui.kor_ans_0.clicked.connect(lambda: kor.check_answer(ui, 0))
    ui.kor_ans_1.clicked.connect(lambda: kor.check_answer(ui, 1))
    ui.kor_ans_2.clicked.connect(lambda: kor.check_answer(ui, 2))
    ui.kor_ans_3.clicked.connect(lambda: kor.check_answer(ui, 3))
    ui.kor_ans_4.clicked.connect(lambda: kor.check_answer(ui, 4))

    # ColorsPlay
    ui.color_clear_btn.clicked.connect(lambda: colors.initiate(ui))
    ui.color_bs_btn.clicked.connect(lambda: colors.backspace(ui))
    ui.color_red_btn.clicked.connect(lambda: colors.add_train(ui, colors.RED))
    ui.color_orange_btn.clicked.connect(lambda: colors.add_train(ui, colors.ORANGE))
    ui.color_peach_btn.clicked.connect(lambda: colors.add_train(ui, colors.PEACH))
    ui.color_beige_btn.clicked.connect(lambda: colors.add_train(ui, colors.BEIGE))
    ui.color_yellow_btn.clicked.connect(lambda: colors.add_train(ui, colors.YELLOW))
    ui.color_ygreen_btn.clicked.connect(lambda: colors.add_train(ui, colors.YGREEN))
    ui.color_green_btn.clicked.connect(lambda: colors.add_train(ui, colors.GREEN))
    ui.color_teal_btn.clicked.connect(lambda: colors.add_train(ui, colors.TEAL))
    ui.color_sblue_btn.clicked.connect(lambda: colors.add_train(ui, colors.SBLUE))
    ui.color_blue_btn.clicked.connect(lambda: colors.add_train(ui, colors.BLUE))
    ui.color_nblue_btn.clicked.connect(lambda: colors.add_train(ui, colors.NBLUE))
    ui.color_violet_btn.clicked.connect(lambda: colors.add_train(ui, colors.VIOLET))
    ui.color_purple_btn.clicked.connect(lambda: colors.add_train(ui, colors.PURPLE))
    ui.color_pink_btn.clicked.connect(lambda: colors.add_train(ui, colors.PINK))
    ui.color_brown_btn.clicked.connect(lambda: colors.add_train(ui, colors.BROWN))
    ui.color_white_btn.clicked.connect(lambda: colors.add_train(ui, colors.WHITE))
    ui.color_gray_btn.clicked.connect(lambda: colors.add_train(ui, colors.GRAY))
    ui.color_black_btn.clicked.connect(lambda: colors.add_train(ui, colors.BLACK))

    # OddOne
    ui.odd1_0.clicked.connect(lambda: oddone.check_answer(ui, 1, 0))
    ui.odd1_1.clicked.connect(lambda: oddone.check_answer(ui, 1, 1))
    ui.odd1_2.clicked.connect(lambda: oddone.check_answer(ui, 1, 2))
    ui.odd1_3.clicked.connect(lambda: oddone.check_answer(ui, 1, 3))
    ui.odd1_4.clicked.connect(lambda: oddone.check_answer(ui, 1, 4))
    ui.odd2_0.clicked.connect(lambda: oddone.check_answer(ui, 2, 0))
    ui.odd2_1.clicked.connect(lambda: oddone.check_answer(ui, 2, 1))
    ui.odd2_2.clicked.connect(lambda: oddone.check_answer(ui, 2, 2))
    ui.odd2_3.clicked.connect(lambda: oddone.check_answer(ui, 2, 3))
    ui.odd2_4.clicked.connect(lambda: oddone.check_answer(ui, 2, 4))
    ui.odd3_0.clicked.connect(lambda: oddone.check_answer(ui, 3, 0))
    ui.odd3_1.clicked.connect(lambda: oddone.check_answer(ui, 3, 1))
    ui.odd3_2.clicked.connect(lambda: oddone.check_answer(ui, 3, 2))
    ui.odd3_3.clicked.connect(lambda: oddone.check_answer(ui, 3, 3))
    ui.odd3_4.clicked.connect(lambda: oddone.check_answer(ui, 3, 4))

    # Patterns
    ui.ptt_ans0.clicked.connect(
        lambda: patterns.check_answer(ui, 0, ui.ptt_ans0.text())
    )
    ui.ptt_ans1.clicked.connect(
        lambda: patterns.check_answer(ui, 1, ui.ptt_ans1.text())
    )
    ui.ptt_ans2.clicked.connect(
        lambda: patterns.check_answer(ui, 2, ui.ptt_ans2.text())
    )
    ui.ptt_ans3.clicked.connect(
        lambda: patterns.check_answer(ui, 3, ui.ptt_ans3.text())
    )

    # Directions
    ui.directions_start.clicked.connect(lambda: directions.initiate(ui))
    ui.up0.clicked.connect(lambda: directions.check_answer(ui, "up0"))
    ui.up1.clicked.connect(lambda: directions.check_answer(ui, "up1"))
    ui.up2.clicked.connect(lambda: directions.check_answer(ui, "up2"))
    ui.down0.clicked.connect(lambda: directions.check_answer(ui, "down0"))
    ui.down1.clicked.connect(lambda: directions.check_answer(ui, "down1"))
    ui.down2.clicked.connect(lambda: directions.check_answer(ui, "down2"))
    ui.left0.clicked.connect(lambda: directions.check_answer(ui, "left0"))
    ui.left1.clicked.connect(lambda: directions.check_answer(ui, "left1"))
    ui.left2.clicked.connect(lambda: directions.check_answer(ui, "left2"))
    ui.right0.clicked.connect(lambda: directions.check_answer(ui, "right0"))
    ui.right1.clicked.connect(lambda: directions.check_answer(ui, "right1"))
    ui.right2.clicked.connect(lambda: directions.check_answer(ui, "right2"))

    # OX Quiz
    ui.ox_tts.setEnabled(False)
    ui.O_btn.setEnabled(False)
    ui.X_btn.setEnabled(False)
    ui.ox_start.clicked.connect(lambda: oxquiz.start_game(ui))
    ui.O_btn.clicked.connect(lambda: oxquiz.check_answer(ui, "O"))
    ui.X_btn.clicked.connect(lambda: oxquiz.check_answer(ui, "X"))

    ########################################################################################

    ui.show()
    sys.exit(app.exec())
