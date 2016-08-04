call %~dp0conda_env

conda create -n pipeline -y python

call activate pipeline

python "%~dp0..\environments\pyblish.py"
python "%~dp0..\environments\ftrack-connect.py"
python "%~dp0..\environments\pipeline.py"

REM need to reactivate to get latest environment variables
call activate pipeline

start python -m pyblish_qml
python -m ftrack_connect
