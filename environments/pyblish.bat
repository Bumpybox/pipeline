call %~dp0conda_env

conda create -n pyblish -y python

call activate pyblish

python "%~dp0..\environments\pyblish.py"

REM need to reactivate to get latest environment variables
call activate pyblish

start python -m pyblish_qml
start cmd
