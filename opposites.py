import os
from PySide6.QtGui import QPixmap
import main, utils

filez = []

KOREAN = {
    "adult_child.jpg": ["어른", "아이"],
    "alone_together1.jpg": ["혼자", "같이"],
    "alone_together2.jpg": ["혼자", "같이"],
    "ask_answer.jpg": ["물어보다", "대답하다"],
    "asleep_awake.jpg": ["잠들다", "깨다"],
    "bad_good.jpg": ["나쁘다", "좋다"],
    "behind_front1.jpg": ["뒤에", "앞에"],
    "behind_front2.jpg": ["뒤에", "앞에"],
    "below_above1.jpg": ["밑에", "위에"],
    "below_above2.jpg": ["밑에", "위에"],
    "big_small1.jpg": ["크다", "작다"],
    "big_small2.jpg": ["크다", "작다"],
    "big_small3.jpg": ["크다", "작다"],
    "big_small4.jpg": ["크다", "작다"],
    "bottom_top.jpg": ["제일 밑에", "제일 위에"],
    "boy_girl.jpg": ["남자아이", "여자아이"],
    "clean_dirty1.jpg": ["깨끗하다", "더럽다"],
    "clean_dirty2.jpg": ["깨끗하다", "더럽다"],
    "closed_open.jpg": ["닫다", "열다"],
    "cold_hot.jpg": ["춥다", "덥다"],
    "cry_laugh1.jpg": ["울다", "웃다"],
    "cry_laugh2.jpg": ["울다", "웃다"],
    "day_night.jpg": ["낮", "밤"],
    "different_same.jpg": ["다르다", "같다"],
    "dirty_clean1.jpg": ["더럽다", "깨끗하다"],
    "dirty_clean2.jpg": ["더럽다", "깨끗하다"],
    "dry_wet1.jpg": ["마르다", "젖다"],
    "dry_wet2.jpg": ["마르다", "젖다"],
    "empty_full.jpg": ["비다", "가득차다"],
    "exciting_boring.jpg": ["신나다", "심심하다"],
    "fast_slow.jpg": ["빠르다", "느리다"],
    "few_many.jpg": ["조금", "많이"],
    "front_back1.jpg": ["앞", "뒤"],
    "front_back2.jpg": ["앞", "뒤"],
    "give_get.jpg": ["주다", "받다"],
    "give_take1.jpg": ["주다", "받다"],
    "give_take2.jpg": ["주다", "받다"],
    "happy_sad.jpg": ["행복하다", "슬프다"],
    "healthy_sick.jpg": ["건강하다", "아프다"],
    "heavy_light.jpg": ["무겁다", "가볍다"],
    "hot_cold.jpg": ["덥다", "춥다"],
    "hungry_full.jpg": ["배고프다", "배부르다"],
    "hungry_thirsty.jpg": ["배고프다", "목마르다"],
    "inside_outside.jpg": ["안에", "밖에"],
    "left_right1.jpg": ["왼쪽", "오른쪽"],
    "left_right2.jpg": ["왼쪽", "오른쪽"],
    "left_right3.jpg": ["왼쪽", "오른쪽"],
    "lie_stand.jpg": ["눕다", "서다"],
    "light_heavy.jpg": ["가볍다", "무겁다"],
    "loud_quiet1.jpg": ["시끄럽다", "조용하다"],
    "loud_quiet2.jpg": ["시끄럽다", "조용하다"],
    "low_high1.jpg": ["낮다", "높다"],
    "low_high2.jpg": ["낮다", "높다"],
    "many_few.jpg": ["많다", "적다"],
    "more_less.jpg": ["많이", "조금"],
    "noisy_quiet.jpg": ["시끄럽다", "조용하다"],
    "off_on.jpg": ["끄다", "켜다"],
    "old_young.jpg": ["늙다", "젊다"],
    "on_under1.jpg": ["위에", "밑에, 아래에"],
    "on_under2.jpg": ["위에", "밑에, 아래에"],
    "open_close1.jpg": ["열다", "닫다"],
    "open_close2.jpg": ["열다", "닫다"],
    "outside_inside1.jpg": ["밖에", "안에"],
    "outside_inside2.jpg": ["밖에", "안에"],
    "pull_push.jpg": ["당기다", "밀다"],
    "push_pull1.jpg": ["밀다", "당기다"],
    "push_pull2.jpg": ["밀다", "당기다"],
    "quiet_loud1.jpg": ["조용하다", "시끄럽다"],
    "quiet_loud2.jpg": ["조용하다", "시끄럽다"],
    "same_different1.jpg": ["같다", "다르다"],
    "same_different2.jpg": ["같다", "다르다"],
    "same_different3.jpg": ["같다", "다르다"],
    "slow_fast.jpg": ["느리다", "빠르다"],
    "small_big1.jpg": ["작다", "크다"],
    "small_big2.jpg": ["작다", "크다"],
    "soft_hard.jpg": ["부드럽다", "단단하다"],
    "stand_sit1.jpg": ["서다", "앉다"],
    "stand_sit2.jpg": ["서다", "앉다"],
    "stand_sit3.jpg": ["서다", "앉다"],
    "start_finish.jpg": ["시작하다", "끝났다"],
    "strong_weak.jpg": ["세다", "약하다"],
    "summer_winter.jpg": ["여름", "겨울"],
    "sun_moon.jpg": ["햇님", "달님"],
    "tall_short1.jpg": ["크다", "작다"],
    "tall_short2.jpg": ["크다", "작다"],
    "top_bottom.jpg": ["꼭대기", "바닥"],
    "untidy_tidy.jpg": ["지저분하다", "깔끔하다"],
    "up_down1.jpg": ["위", "아래"],
    "up_down2.jpg": ["위", "아래"],
    "weak_strong.jpg": ["약하다", "강하다"],
    "whole_part.jpg": ["전부", "일부"],
    "woman_man.jpg": ["여자", "남자"],
}


def initiate(ui):
    global filez
    filez = os.listdir("resources/opposites")
    words = []
    for file in filez:
        word_temp = file.replace(".jpg", "")
        word = word_temp.replace("_", "  vs.  ")
        words.append(word)
    for word in words:
        if word[-1].isdigit():
            word = word.replace(word[-1], f" #{word[-1]}")
        ui.opp_combo.addItem(word)

    index = ui.opp_combo.currentIndex()
    ui.opp_img.setPixmap(QPixmap(f"resources/opposites/{filez[index]}"))
    ui.opp_kor_1.setText(KOREAN[filez[index]][0])
    ui.opp_kor_2.setText(KOREAN[filez[index]][1])


def combo_select(ui):
    index = ui.opp_combo.currentIndex()
    ui.opp_img.setPixmap(QPixmap(f"resources/opposites/{filez[index]}"))
    ui.opp_kor_1.setText(KOREAN[filez[index]][0])
    ui.opp_kor_2.setText(KOREAN[filez[index]][1])


def prev(ui):
    index = ui.opp_combo.currentIndex()
    if index != 0:
        ui.opp_combo.setCurrentIndex(index - 1)
    else:
        ui.opp_combo.setCurrentIndex(len(filez) - 1)


def next(ui):
    index = ui.opp_combo.currentIndex()
    if index != len(filez) - 1:
        ui.opp_combo.setCurrentIndex(index + 1)
    else:
        ui.opp_combo.setCurrentIndex(0)


def playmp3(ui, kor: bool = False):
    index = ui.opp_combo.currentIndex()
    global filez
    currentFile = filez[index]
    currentFile = currentFile.replace(".jpg", "")
    if currentFile[-1].isdigit():
        currentFile = currentFile.replace(currentFile[-1], "")
    eng_mp3File = f"resources/opposites/mp3/{currentFile}.mp3"
    kor_mp3File = f"resources/opposites/mp3/kor/kor_{currentFile}.mp3"
    if kor:
        utils.play_MP3(kor_mp3File)
    else:
        utils.play_MP3(eng_mp3File)
