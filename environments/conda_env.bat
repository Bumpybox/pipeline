IF EXIST %~dp0..\miniconda GOTO INSTALLEXISTS
%~dp0..\miniconda.exe /RegisterPython=0 /AddToPath=0 /S /D=%~dp0..\miniconda
:INSTALLEXISTS

set PATH=%~dp0..\miniconda;%~dp0..\miniconda\Scripts;%PATH%