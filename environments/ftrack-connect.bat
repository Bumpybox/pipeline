call %~dp0conda_env

conda create -n ftrack-connect -y python

call activate ftrack-connect

python "%~dp0..\environments\ftrack-connect.py"

REM need to reactivate to get latest environment variables
call activate ftrack-connect

python -m ftrack_connect
