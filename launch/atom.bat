call "%~dp0..\environments\conda_env.bat"

conda create -n atom -y python

call activate atom

python %~dp0atom.py