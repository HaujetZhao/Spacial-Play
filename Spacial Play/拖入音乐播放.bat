@echo off

:: 作者：淳帅二代
:: 日期：2021 年 3 月 6 日

for %%i in (%*) do (
	echo 正在播放：%%i
	cd %%~dpi
	python 空间播放音乐.py %%i
)

pause
