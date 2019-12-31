# -*- coding: utf-8 -*-
from aip import AipSpeech
import os

APP_ID = '18139977'
API_KEY = 'G8LLOmt8fivpBX0RPQNzQKwc'
SECRET_KEY = 'x2LbbQFHepdaI3fnxsk7LBbEYh9KlH7S'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    os.system(f"ffmpeg -y  -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()

# 识别本地文件
ret = client.asr(get_file_content('1.m4a'), 'pcm', 16000, {
    'dev_pid': 1536,
})

print(ret)