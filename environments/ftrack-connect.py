import os

dst = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'miniconda',
                                   'envs', 'ftrack-connect', 'etc', 'conda',
                                   'activate.d', 'env_vars.bat')

if not os.path.exists(os.path.dirname(dst)):
    os.makedirs(os.path.dirname(dst))

f = open(dst, 'w')
f.write('set PYTHONPATH=%PYTHONPATH%;%~dp0..\..\..\..\..\..\pythonpath\n')
f.write('set FTRACK_CONNECT_PLUGIN_PATH=%FTRACK_CONNECT_PLUGIN_PATH%;')
f.write('%CONDA_DEFAULT_ENV%\n')
f.close()
