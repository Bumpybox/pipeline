cd %~dp0..

call environments\conda_env

call activate pipeline

python %~dp0atom.py
