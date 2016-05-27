cd %~dp0

call conda_environment

REM creates a known environment to use git from
IF EXIST %~dp0miniconda/envs/git GOTO GITEXISTS
conda env create --force -f %~dp0environments/git.yml
:GITEXISTS

REM updating repo
start /W %~dp0miniconda\envs\git\Library\bin\git.exe pull

REM create requested environment
conda env create --force -f %1
pause
