cd %~dp0

call conda_env

conda env create -f environments\ftrack-connect.yml

python environments\ftrack-connect.py

call activate ftrack-connect

pip install PySide
pip install --editable git+https://bitbucket.org/ftrack/ftrack-connect.git#egg=ftrack_connect
cd %~dp0..\src\ftrack-connect\source\ftrack_connect\ui
%~dp0..\miniconda\envs\ftrack-connect\Lib\site-packages\PySide\pyside-rcc.exe -o resource.py %~dp0..\src\ftrack-connect\resource\resource.qrc

cd %~dp0..
pip install --editable git+https://bitbucket.org/ftrack/ftrack-connect-foundry.git#egg=ftrack_connect_foundry
pip install --editable git+https://bitbucket.org/ftrack/ftrack-connect-nuke.git#egg=ftrack_connect_nuke
goto commentout
pip install git+https://bitbucket.org/ftrack/ftrack-connect-nuke-studio.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-hieroplayer.git

pip install git+https://bitbucket.org/ftrack/ftrack-connect-maya.git

pip install git+https://bitbucket.org/ftrack/ftrack-connect-adobe.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-photoshop.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-after-effects.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-premiere.git
:commentout
python -m ftrack_connect

start cmd
