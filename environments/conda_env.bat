IF EXIST %~dp0..\miniconda GOTO INSTALLEXISTS
SET "FILENAME=%~dp0..\miniconda.exe"
SET "URL=https://repo.continuum.io/miniconda/Miniconda2-latest-Windows-x86_64.exe"
powershell "Import-Module BitsTransfer; Start-BitsTransfer '%URL%' '%FILENAME%'"
%~dp0..\miniconda.exe /RegisterPython=0 /AddToPath=0 /S /D=%~dp0..\miniconda
:INSTALLEXISTS

set PATH=%~dp0..\miniconda;%~dp0..\miniconda\Scripts;%PATH%