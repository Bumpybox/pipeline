set PATH=%~dp0miniconda;%~dp0miniconda\Scripts
call activate pipeline
python %~dp0atom_launch.py
