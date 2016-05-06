cd %~dp0
start /W %~dp0vendors\git\bin\git.exe pull
%~dp0vendors\Python27\python.exe %~dp0repositories.py
