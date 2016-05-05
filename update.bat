cd %~dp0
start /W git pull
%~dp0/vendors/Python27/python.exe %~dp0/repositories.py
