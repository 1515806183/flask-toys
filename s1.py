# -*- coding: utf-8 -*-
from aip import AipSpeech

APP_ID = '18139977'
API_KEY = 'G8LLOmt8fivpBX0RPQNzQKwc'
SECRET_KEY = 'x2LbbQFHepdaI3fnxsk7LBbEYh9KlH7S'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('小哥哥来玩呀', 'zh', 1, {
    'vol': 5,
})

print(result)

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)