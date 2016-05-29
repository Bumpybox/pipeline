cd %~dp0

call conda_env

conda env create -f environments\ftrack-connect.yml

python environments\ftrack-connect.py

call activate ftrack-connect

pip install PySide
pip install git+https://bitbucket.org/ftrack/ftrack-connect.git

pip install git+https://bitbucket.org/ftrack/ftrack-connect-foundry.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-nuke.git
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
