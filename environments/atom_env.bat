call %~dp0conda_env

conda create -n atom_env -y python

call activate atom_env

python "%~dp0pyblish_env.py" --setup
python "%~dp0ftrack_connect_env.py" --setup
python "%~dp0pipeline_env.py" --setup
python "%~dp0atom_env.py" --setup

REM need to reactivate to get latest environment variables
call activate atom_env

python %~dp0atom_env.py --launch
