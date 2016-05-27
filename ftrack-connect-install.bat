cd %~dp0

call conda_environment

conda env create -f environments\ftrack-connect.yml

call activate ftrack-connect

call ftrack_connect_environment

goto commentout
pip install git+https://bitbucket.org/ftrack/ftrack-connect.git

pip install git+https://bitbucket.org/ftrack/ftrack-connect-foundry.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-nuke.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-nuke-studio.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-hieroplayer.git

pip install git+https://bitbucket.org/ftrack/ftrack-connect-maya.git

pip install git+https://bitbucket.org/ftrack/ftrack-connect-adobe.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-hieroplayer.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-photoshop.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-after-effects.git
pip install git+https://bitbucket.org/ftrack/ftrack-connect-premiere.git

python -m ftrack_connect
:commentout
pause
