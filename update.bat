cd %~dp0

REM downloading the miniconda install executable seems very slow
REM SET "FILENAME=%~dp0miniconda.exe"
REM bitsadmin.exe /transfer "Miniconda Download" https://repo.continuum.io/miniconda/Miniconda2-latest-Windows-x86_64.exe "%FILENAME%"

IF EXIST %~dp0miniconda GOTO INSTALLEXISTS
%~dp0miniconda.exe /RegisterPython=0 /AddToPath=0 /S /D=%~dp0miniconda
:INSTALLEXISTS

set PATH=%~dp0miniconda;%~dp0miniconda\Scripts

conda install git -y
start /W %~dp0miniconda\Library\bin\git.exe pull

conda env create -f %~dp0environment.yml
