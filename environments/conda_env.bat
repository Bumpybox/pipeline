REM downloading the miniconda install executable seems very slow
REM SET "FILENAME=%~dp0miniconda.exe"
REM bitsadmin.exe /transfer "Miniconda Download" https://repo.continuum.io/miniconda/Miniconda2-latest-Windows-x86_64.exe "%FILENAME%"

IF EXIST %~dp0..\miniconda GOTO INSTALLEXISTS
%~dp0..\miniconda.exe /RegisterPython=0 /AddToPath=0 /S /D=%~dp0..\miniconda
:INSTALLEXISTS

set PATH=%~dp0..\miniconda;%~dp0..\miniconda\Scripts;%PATH%

conda update conda -y
