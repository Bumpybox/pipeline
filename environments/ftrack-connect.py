import os

dst = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'miniconda',
                                   'envs', 'ftrack-connect', 'etc', 'conda',
                                   'activate.d', 'env_vars.bat')

if not os.path.exists(os.path.dirname(dst)):
    os.makedirs(os.path.dirname(dst))

f = open(dst, 'w')
f.write(r'set PYTHONPATH=%PYTHONPATH%;%~dp0..\..\..\..\..\..\pythonpath')
f.write('\n')
f.write(r'set FTRACK_CONNECT_PLUGIN_PATH=%FTRACK_CONNECT_PLUGIN_PATH%;')
f.write(r'%~dp0..\..\..\..\..\..\src\ftrack-connect;')
f.write(r'%~dp0..\..\..\..\..\..\src\ftrack-connect-foundry;')
f.write(r'%~dp0..\..\..\..\..\..\src\ftrack-connect-nuke')
f.close()
