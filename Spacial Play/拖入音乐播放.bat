@echo off

:: ���ߣ���˧����
:: ���ڣ�2021 �� 3 �� 6 ��

cd %~dp0

for %%i in (%*) do (
	echo ���ڲ��ţ�%%i
	python �ռ䲥������.py %%i
)

pause
