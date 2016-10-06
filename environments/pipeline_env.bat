call %~dp0conda_env

conda create -n pipeline_env -y python

call activate pipeline_env

python "%~dp0..\environments\pyblish_env.py" --setup %*
python "%~dp0..\environments\ftrack_connect_env.py" --setup %*
python "%~dp0..\environments\pipeline_env.py" --setup %*

REM need to reactivate to get latest environment variables
call activate pipeline

start python "%~dp0..\environments\pyblish_env.py" --launch %*
start python "%~dp0..\environments\ftrack_connect_env.py" --launch %*
