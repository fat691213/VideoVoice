import moviepy.editor as mp
import speech_recognition as sr

# 1. 讀取影片並提取音訊
video = mp.VideoFileClip("身份資訊.mp4")
video.audio.write_audiofile("extracted_audio.wav")

# 2. 使用語音辨識將音訊轉成文字
recognizer = sr.Recognizer()
with sr.AudioFile("extracted_audio.wav") as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data, language="zh-TW")
    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("✅ 轉錄完成，已儲存為 transcription.txt")
except sr.UnknownValueError:
    print("⚠️ 無法辨識音訊內容")
except sr.RequestError as e:
    print(f"⚠️ 無法連接 Google 語音辨識服務：{e}")
