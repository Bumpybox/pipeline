cd %~dp0

REM downloading the miniconda install executable seems very slow
REM SET "FILENAME=%~dp0miniconda.exe"
REM bitsadmin.exe /transfer "Miniconda Download" https://repo.continuum.io/miniconda/Miniconda2-latest-Windows-x86_64.exe "%FILENAME%"

IF EXIST %~dp0miniconda GOTO INSTALLEXISTS
%~dp0miniconda.exe /RegisterPython=0 /AddToPath=0 /S /D=%~dp0miniconda
:INSTALLEXISTS

set PATH=%~dp0miniconda;%~dp0miniconda\Scripts;%PATH%

REM creates a known environment to use git from
IF EXIST %~dp0miniconda/envs/git GOTO GITEXISTS
conda env create --force -f %~dp0environments/git.yml
:GITEXISTS

REM updating repo
start /W %~dp0miniconda\envs\git\Library\bin\git.exe pull

REM create requested environment
if "%1"=="" goto NOARGUMENTS
conda env create --force -f %1
exit
:NOARGUMENTS

conda env create --force -f %~dp0environments/pipeline.yml
