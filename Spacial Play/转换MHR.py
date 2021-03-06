'''
脚本作用：使用 OpenAl soft 将 51 个 Impulse responses archive 文件转换成 OpenAl 能够
直接使用的 mhr 文件，每个 mhr 文件都是不同的 HRTF 函数映射

Impulse responses archive 文件来自：
http://recherche.ircam.fr/equipes/salles/listen/download.html
'''

import os
import re
import subprocess
import shlex
from pathlib import Path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import zipfile

alSoft路径 = 'openal-soft-1.15.1-bin'
# alSoft路径 = 'openal-soft-1.21.1-bin'

def文件路径 = os.path.join(alSoft路径, 'hrtf_defs', 'IRC_1005.def')
IRC路径 = Path(alSoft路径) / 'IRC'
archive路径 = 'Impulse responses archive'
mhr路径 = 'MinPHR'

if not IRC路径.exists():
    os.makedirs(IRC路径)

for 文件名 in os.listdir(archive路径):
    
    # 先清空 irc 文件夹
    print(f'\n清空 irc 文件夹中')
    for root, folders, files in os.walk(IRC路径):
        for file in files:
            os.remove(Path(root) / file)
    
    
    路径名 = Path(archive路径) / 文件名
    print(f'解压文件中：{路径名}')
    with zipfile.ZipFile(路径名) as 压缩文件:
        压缩文件.extractall(path=IRC路径)
    
    IRC名字 = os.path.splitext(文件名)[0]
    with open(def文件路径, 'r') as def文件:
        def内容 = def文件.read()
        新def内容 = re.sub('IRC_\d{4}', IRC名字, def内容)
    with open(def文件路径, 'w') as def文件:
        def文件.write(新def内容)
    
    命令 = rf'''"./{alSoft路径}/makehrtf.exe" -m
                "-i=hrtf_defs\\IRC_1005.def" 
                "-o=..\\{mhr路径}\\01D_OpenAL_Soft_HRTF_{IRC名字}_%r.mhr"'''
    # 命令 = rf'''./{alSoft路径}/makemhr.exe
    #             -i "hrtf_defs\\IRC_1005.def" 
    #             -o "..\\{mhr路径}\\03D_OpenAL_Soft_HRTF_{IRC名字}_%r.mhr"'''
    print(shlex.split(命令))
    print(alSoft路径)
    subprocess.run(shlex.split(命令), cwd=f'./{alSoft路径}')
    
    
    
    
    
    
