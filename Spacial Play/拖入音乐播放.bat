@echo off

:: ���ߣ���˧����
:: ���ڣ�2021 �� 3 �� 6 ��

for %%i in (%*) do (
	echo ���ڲ��ţ�%%i
	cd %%~dpi
	python �ռ䲥������.py %%i
)

pause
