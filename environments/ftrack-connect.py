import os
import subprocess
import sys

repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = os.path.basename(os.path.dirname(sys.executable))

# install PySide
subprocess.call(["pip", "install", "PySide"])

# install ftrack-connect
subprocess.call(["pip", "install", "--editable",
                 "git+https://bitbucket.org/ftrack/ftrack-connect.git" +
                 "#egg=ftrack_connect"], cwd=repo_path)

rcc_exe = os.path.join(repo_path, "miniconda", "envs", env, "Lib",
                       "site-packages", "PySide", "pyside-rcc.exe")
resource_py = os.path.join(repo_path, "src", "ftrack-connect", "source",
                           "ftrack_connect", "ui", "resource.py")
resource_qrc = os.path.join(repo_path, "src", "ftrack-connect", "resource",
                            "resource.qrc")
subprocess.call([rcc_exe, "-o", resource_py, resource_qrc])

# install ftrack-connect-foundry
subprocess.call(["pip", "install", "--editable",
                 "git+https://bitbucket.org/ftrack/ftrack-connect-foundry" +
                 ".git#egg=ftrack-connect-foundry"], cwd=repo_path)

# install ftrack-connect-nuke
subprocess.call(["pip", "install", "--editable",
                 "git+https://bitbucket.org/ftrack/ftrack-connect-nuke.git" +
                 "#egg=ftrack-connect-nuke"], cwd=repo_path)

# install ftrack-connect-maya
subprocess.call(["pip", "install", "--editable",
                 "git+https://bitbucket.org/ftrack/ftrack-connect-maya.git" +
                 "#egg=ftrack-connect-maya"], cwd=repo_path)

# setup environment variables
dst = os.path.join(os.path.dirname(os.path.dirname(__file__)), "miniconda",
                   "envs", env, "etc", "conda", "activate.d",
                   "env_vars.bat")

if not os.path.exists(os.path.dirname(dst)):
    os.makedirs(os.path.dirname(dst))

f = open(dst, "w")

python_path = r"set PYTHONPATH=%PYTHONPATH%;%~dp0..\..\..\..\..\..\pythonpath;"
python_path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-nuke\source;"
python_path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect\source;"
python_path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-foundry\source;"
python_path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-maya\source;"
python_path += r"%~dp0..\..\..\Lib\site-packages"

plugin_path = r"set FTRACK_CONNECT_PLUGIN_PATH=%FTRACK_CONNECT_PLUGIN_PATH%;"
plugin_path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect;"
plugin_path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-foundry;"
plugin_path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-nuke;"
plugin_path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-maya;"
plugin_path += r"%~dp0..\..\..\..\..\..\environments"

nuke_plugin = r"set FTRACK_CONNECT_NUKE_PLUGINS_PATH="
nuke_plugin += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-nuke\resource"

maya_plugin = r"set FTRACK_CONNECT_MAYA_PLUGINS_PATH="
maya_plugin += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-maya\resource"

f.write(python_path)
f.write("\n")
f.write(plugin_path)
f.write("\n")
f.write(nuke_plugin)
f.write("\n")
f.write(maya_plugin)
