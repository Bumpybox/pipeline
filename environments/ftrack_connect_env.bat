call %~dp0conda_env

conda create -n ftrack_connect_env -y python

call activate ftrack_connect_env

python "%~dp0..\environments\ftrack_connect_env.py" --setup %*

REM need to reactivate to get latest environment variables
call activate ftrack_connect_env

start python "%~dp0..\environments\ftrack_connect_env.py" --launch %*
