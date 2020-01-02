# -*- coding: utf-8 -*-
from aip import AipNlp
import os

APP_ID = '18139977'
API_KEY = 'G8LLOmt8fivpBX0RPQNzQKwc'
SECRET_KEY = 'x2LbbQFHepdaI3fnxsk7LBbEYh9KlH7S'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text1 = "你姓什么"

text2 = "你贵姓"

""" 调用短文本相似度 """
client.simnet(text1, text2)

""" 如果有可选参数 """
options = {}
options["model"] = "CNN"

""" 带参数调用短文本相似度 """
ret = client.simnet(text1, text2, options)

print(ret)