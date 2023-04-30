import os
from gtts import gTTS


files = os.listdir("resources/eng2")
words = []
for file in files:
    word_temp = file.replace(".jpg", "")
    words.append(word_temp)


# tts = gTTS("0", lang="ko")
# tts.save("hellso.mp3")

for word in words:
    if "_" in word:
        wordz = word.replace("_", " ")
    else:
        wordz = word
    tts = gTTS(wordz, lang="en")
    tts.save(f"{word}.mp3")
