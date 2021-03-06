'''
脚本作用：使用 OpenAl 将 51 个 Impulse responses archive 转换生成的 mhr 文件依次
测试其空间效果
'''

import os
import subprocess
import shlex
import configparser
import glob
import chardet
from pathlib import Path
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def 得到文件编码(file):
    with open(file, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']

mhr文件夹路径名 = os.path.abspath('MinPHR')
ini配置文件路径名 = Path(os.environ['appdata']) / 'alsoft.ini'

# 避免配置文件不存在
if not os.path.exists(ini配置文件路径名):
    with open(ini配置文件路径名, encoding='utf-8') as 配置文件:
        配置文件.write(rf'''[General]
                   hrtf=true
                   hrtf-paths="{mhr文件夹路径名},"
                   default-hrtf=03D_OpenAL_Soft_HRTF_IRC_1002_44100''')

for MHR文件 in glob.glob(rf'{mhr文件夹路径名}\*.mhr'):
    MHR文件路径名 = os.path.abspath(MHR文件)
    MHR文件路径 = os.path.dirname(MHR文件路径名)
    MHR文件名 = os.path.basename(MHR文件)
    MHR文件主名 = os.path.splitext(MHR文件名)[0]
    
    配置 = configparser.ConfigParser()
    try:
        配置.read(ini配置文件路径名, 得到文件编码(ini配置文件路径名))
    except:
        配置['General'] = {'hrtf':'true'}
    
    hrtf_path = 配置['General']['hrtf-paths'].strip('"').split(',')
    if MHR文件路径 not in hrtf_path:
        hrtf_path.append(MHR文件路径)
        配置['General']['hrtf-paths'] = f'"{"".join(MHR文件路径)}"'
    配置['General']['default-hrtf'] = MHR文件主名
    with open(ini配置文件路径名, 'w', encoding='utf-8') as f:
        配置.write(f)
    
    print(f'此次使用的 mhr 文件是：{MHR文件主名}')
    命令 = f'python MHR测试.py'
    subprocess.run(shlex.split(命令))
    input('p')
