"""
脚本作用：使用 OpenAl 将播放音频，施加空间旋转效果，用于测试 hrtf
"""

import importlib
import time
import tempfile
import subprocess
import shlex
import math
import sys
import os
from pathlib import Path
import argparse
import configparser
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.environ['path'] = os.pathsep.join([  os.path.dirname(
                                            os.path.abspath(
                                                __file__)), 
                                        os.getenv('Path')])


def 自动配置HRTF():
    MHR所在文件夹 = os.path.abspath('MinPHR')
    MHR文件主名 = os.path.splitext('oalsoft_hrtf_IRC_1014_44100.mhr')[0]
    APPDATA文件夹 = os.environ['appdata']
    ini文件路径 = Path(APPDATA文件夹) / 'alsoft.ini'
    
    if not os.path.exists(ini文件路径):
        with open(ini文件路径) as 配置文件:
            配置文件.write(rf'''[General]
                    hrtf=true
                    hrtf-paths="{MHR所在文件夹},"
                    default-hrtf={MHR文件主名}''')
    else:
        配置 = configparser.ConfigParser()
        try:
            配置.read(ini文件路径)
        except:
            配置['General'] = {'hrtf': 'true'}

        hrtf_path = 配置['General']['hrtf-paths'].strip('"').split(',')
        if MHR所在文件夹 not in hrtf_path:
            hrtf_path.append(MHR所在文件夹)
            配置['General']['hrtf-paths'] = f'"{",".join(hrtf_path)}"'
        配置['General']['default-hrtf'] = MHR文件主名
        with open(ini文件路径, 'w') as f:
            配置.write(f)

# 如果用户还没有配置 openal 的 hrtf 设置，那就需要这里自动配置一下，再导入 openal
自动配置 = True
if 自动配置:
    自动配置HRTF()
import openal


def 得到临时左右音频文件(音频文件):
    临时左声道文件 = 'temp_left.wav'
    临时右声道文件 = 'temp_right.wav'

    命令 = ['ffmpeg', '-hide_banner', '-y',
        '-i', 音频文件,
        '-ac', '1',
        '-s', '44100',
        '-map_channel', '0.0.0',
        临时左声道文件]
    subprocess.run(命令, capture_output=True)
    命令 = ['ffmpeg', '-hide_banner', '-y',
        '-i', 音频文件,
        '-ac', '1',
        '-s', '44100',
        '-map_channel', '0.0.1',
        临时右声道文件]
    return 临时左声道文件, 临时右声道文件
    

parser = argparse.ArgumentParser(
    description='''功能：用 openal 空间音频播放音乐''',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('Media', type=str, help='音视频文件')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

# 检查音频文件是否存在
音频文件 = args.Media
if not os.path.exists(音频文件):
    print('音频文件不存在')
    exit()

# 将音频文件分成两个单独的单声道文件
临时左声道文件, 临时右声道文件 = 得到临时左右音频文件(音频文件)

# 设置距离直径
r = 1

# 打开两个声音源
左后源 = openal.oalOpen(临时左声道文件)
右后源 = openal.oalOpen(临时右声道文件)

# 初始化两个音源的三维位置
左后源.set_position((r, r * 1, 0))
右后源.set_position((r, -r * 1, 0))

# 开始播放
左后源.play()
右后源.play()

# 在这里睡眠，直到播放完毕
# while 左后源.get_state() == openal.AL_PLAYING or \
#         右后源.get_state() == openal.AL_PLAYING:
#     time.sleep(1)

# 在这里变换音源的位置
angle = 0
while 左后源.get_state() == openal.AL_PLAYING or \
        右后源.get_state() == openal.AL_PLAYING:
    rx = r * math.cos((angle + 60) / 180 * math.pi)
    ry = r * math.sin((angle + 60) / 180 * math.pi)
    
    lx = r * math.cos((angle + 120) / 180 * math.pi)
    ly = r * math.sin((angle + 120) / 180 * math.pi)
    
    右后源.set_position((rx, ry, 0))
    左后源.set_position((lx, ly, 0))
    
    angle = (angle + 1) % 360
    time.sleep(8 / 360)

# 安全清理 openal
openal.oalQuit()



