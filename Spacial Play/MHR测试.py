"""
脚本作用：使用 OpenAl 将播放音频，施加空间旋转效果，用于测试 hrtf
"""

import openal
import importlib
import time
import math
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

r = 1
声源 = openal.oalOpen('lone_ranger_left.wav')

声源.play()

angle = 0
for angle in range(360 * 2):
    x = r * math.cos((angle + 60) / 180 * math.pi)
    y = r * math.sin((angle + 60) / 180 * math.pi)

    声源.set_position((x, y, 0))

    time.sleep(3 / 360)

openal.oalQuit()



