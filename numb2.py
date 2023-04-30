import utils

NUMB_WORDS = [
    ["zero", "영"],
    ["one", "일"],
    ["two", "이"],
    ["three", "삼"],
    ["four", "사"],
    ["five", "오"],
    ["six", "육"],
    ["seven", "칠"],
    ["eight", "팔"],
    ["nine", "구"],
    ["ten", "십"],
    ["eleven", "십일"],
    ["twelve", "십이"],
    ["thirteen", "십삼"],
    ["fourteen", "십사"],
    ["fifteen", "십오"],
    ["sixteen", "십육"],
    ["seventeen", "십칠"],
    ["eighteen", "십팔"],
    ["nineteen", "십구"],
    ["twenty", "이십"],
    ["twenty-one", "이십일"],
    ["twenty-two", "이십이"],
    ["twenty-three", "이십삼"],
    ["twenty-four", "이십사"],
    ["twenty-five", "이십오"],
    ["twenty-six", "이십육"],
    ["twenty-seven", "이십칠"],
    ["twenty-eight", "이십팔"],
    ["twenty-nine", "이십구"],
    ["thirty", "삼십"],
    ["thirty-one", "삼십일"],
    ["thirty-two", "삼십이"],
    ["thirty-three", "삼십삼"],
    ["thirty-four", "삼십사"],
    ["thirty-five", "삼십오"],
    ["thirty-six", "삼십육"],
    ["thirty-seven", "삼십칠"],
    ["thirty-eight", "삼십팔"],
    ["thirty-nine", "삼십구"],
    ["fourty", "사십"],
    ["fourty-one", "사십일"],
    ["fourty-two", "사십이"],
    ["fourty-three", "사십삼"],
    ["fourty-four", "사십사"],
    ["fourty-five", "사십오"],
    ["fourty-six", "사십육"],
    ["fourty-seven", "사십칠"],
    ["fourty-eight", "사십팔"],
    ["fourty-nine", "사십구"],
    ["fifty", "오십"],
    ["fifty-one", "오십일"],
    ["fifty-two", "오십이"],
    ["fifty-three", "오십삼"],
    ["fifty-four", "오십사"],
    ["fifty-five", "오십오"],
    ["fifty-six", "오십육"],
    ["fifty-seven", "오십칠"],
    ["fifty-eight", "오십팔"],
    ["fifty-nine", "오십구"],
    ["sixty", "육십"],
    ["sixty-one", "육십일"],
    ["sixty-two", "육십이"],
    ["sixty-three", "육십삼"],
    ["sixty-four", "육십사"],
    ["sixty-five", "육십오"],
    ["sixty-six", "육십육"],
    ["sixty-seven", "육십칠"],
    ["sixty-eight", "육십팔"],
    ["sixty-nine", "육십구"],
    ["seventy", "칠십"],
    ["seventy-one", "칠십일"],
    ["seventy-two", "칠십이"],
    ["seventy-three", "칠십삼"],
    ["seventy-four", "칠십사"],
    ["seventy-five", "칠십오"],
    ["seventy-six", "칠십육"],
    ["seventy-seven", "칠십칠"],
    ["seventy-eight", "칠십팔"],
    ["seventy-nine", "칠십구"],
    ["eighty", "팔십"],
    ["eighty-one", "팔십일"],
    ["eighty-two", "팔십이"],
    ["eighty-three", "팔십삼"],
    ["eighty-four", "팔십사"],
    ["eighty-five", "팔십오"],
    ["eighty-six", "팔십육"],
    ["eighty-seven", "팔십칠"],
    ["eighty-eight", "팔십팔"],
    ["eighty-nine", "팔십구"],
    ["ninety", "구십"],
    ["ninety-one", "구십일"],
    ["ninety-two", "구십이"],
    ["ninety-three", "구십삼"],
    ["ninety-four", "구십사"],
    ["ninety-five", "구십오"],
    ["ninety-six", "구십육"],
    ["ninety-seven", "구십칠"],
    ["ninety-eight", "구십팔"],
    ["ninety-nine", "구십구"],
    ["hundred", "백"],
]


DEFAULT_STYLE = """
background-color: rgb(130, 160, 160);
border:1px solid rgb(120, 150, 150);
border-radius:30px;
color: rgb(77, 133, 133);
"""

SELECTED_STYLE = """
background-color: rgb(140, 175, 145);
border:1px solid rgb(120, 150, 150);
border-radius:30px;
color: rgb(55, 144, 122);
"""


def numb_select(ui, numb: int):
    prev_numb = ui.numb2_number.text()
    prev_numb_btn = getattr(ui, f"numb2_{prev_numb}")
    prev_numb_btn.setStyleSheet(DEFAULT_STYLE)

    ui.numb2_number.setText(str(numb))
    ui.numb2_number_kor.setText(NUMB_WORDS[numb][1])
    ui.numb2_number_eng.setText(NUMB_WORDS[numb][0])
    current_numb_btn = getattr(ui, f"numb2_{numb}")
    current_numb_btn.setStyleSheet(SELECTED_STYLE)


def play_mp3(ui, lang: str):
    language = ["eng", "kor"]
    if lang not in language:
        return

    numb = ui.numb2_number.text()

    filename = f"resources/numb2/{lang}/{lang}_{numb}.mp3"

    utils.play_MP3(filename)
