# -*- coding: utf-8 -*-
from aip import AipSpeech
import time, os

APP_ID = '18139977'
API_KEY = 'G8LLOmt8fivpBX0RPQNzQKwc'
SECRET_KEY = 'x2LbbQFHepdaI3fnxsk7LBbEYh9KlH7S'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def text2audio(text):
    filename  = f"{time.time()}.mp3"
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
        'spd': 3,
        'pit': 7,
        "per": 4
    })

    if not isinstance(result, dict):
        with open(filename, 'wb') as f:
            f.write(result)

    return filename

# print(text2audio('今天风和日历'))


def audio2text(filename):
    # 读取文件
    def get_file_content(filename):
        os.system(f"ffmpeg -y  -i {filename} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filename}.pcm")
        with open(f"{filename}.pcm", 'rb') as fp:
            return fp.read()

    # 识别本地文件
    ret = client.asr(get_file_content(filename), 'pcm', 16000, {
        'dev_pid': 1536,
    })

    return ret['result'][0]

text = audio2text('1.m4a')
print(text)

if text == '你的名字叫什么':
    text = '我的名字叫peach'

filename = text2audio(text)

