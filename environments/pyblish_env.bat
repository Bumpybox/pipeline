call %~dp0conda_env

conda create -n pyblish_env -y python

call activate pyblish_env

python "%~dp0..\environments\pyblish_env.py" --setup

REM need to reactivate to get latest environment variables
call activate pyblish_env

start python "%~dp0..\environments\pyblish_env.py" --launch
