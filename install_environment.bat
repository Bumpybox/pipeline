cd %~dp0..

call environments\conda_env

python %~dp0install_environment.py
