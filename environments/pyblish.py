import os
import subprocess
import sys

repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = os.path.basename(os.path.dirname(sys.executable))

# install pyblish-base
subprocess.call(["pip", "install", "--editable",
                 "git+https://github.com/pyblish/pyblish-base.git" +
                 "#egg=pyblish-base"], cwd=repo_path)

# install PyQt5 not in developer mode
subprocess.call(["pip", "install",
                 "git+https://github.com/pyqt/python-qt5.git"],
                cwd=repo_path)

# install pyblish-qml
subprocess.call(["pip", "install", "--editable",
                 "git+https://github.com/pyblish/pyblish-qml.git" +
                 "#egg=pyblish-qml"], cwd=repo_path)

# install pyblish-nuke
subprocess.call(["pip", "install", "--editable",
                 "git+https://github.com/pyblish/pyblish-nuke.git" +
                 "#egg=pyblish-nuke"], cwd=repo_path)

# install pyblish-maya
subprocess.call(["pip", "install", "--editable",
                 "git+https://github.com/pyblish/pyblish-maya.git" +
                 "#egg=pyblish-maya"], cwd=repo_path)

# install pyblish-maya
subprocess.call(["pip", "install", "--editable",
                 "git+https://github.com/pyblish/pyblish-houdini.git" +
                 "#egg=pyblish-houdini"], cwd=repo_path)

# install pyblish-standalone
subprocess.call(["pip", "install", "--editable",
                 "git+https://github.com/pyblish/pyblish-standalone.git" +
                 "#egg=pyblish-standalone"], cwd=repo_path)

# setup environment variables
dst = os.path.join(os.path.dirname(os.path.dirname(__file__)), "miniconda",
                   "envs", env, "etc", "conda", "activate.d",
                   "env_vars.bat")

if not os.path.exists(os.path.dirname(dst)):
    os.makedirs(os.path.dirname(dst))

f = None
if os.path.exists(dst):
    f = open(dst, "a")
else:
    f = open(dst, "w")

path = r"set PYTHONPATH=%PYTHONPATH%;"
path += r"%~dp0..\..\..\..\..\..\pythonpath;"
path += r"%~dp0..\..\..\..\..\..\src\pyblish-base;"
path += r"%~dp0..\..\..\..\..\..\src\pyblish-qml;"
path += r"%~dp0..\..\..\..\..\..\src\pyblish-nuke;"
path += r"%~dp0..\..\..\..\..\..\src\pyblish-maya;"
path += r"%~dp0..\..\..\..\..\..\src\pyblish-standalone;"
path += r"%~dp0..\..\..\..\..\..\src\pyblish-maya\pyblish_maya\pythonpath;"
path += r"%~dp0..\..\..\Lib\site-packages"

f.write(path)
f.write("\n")

path = r"set NUKE_PATH=%NUKE_PATH%;"
path += r"%~dp0..\..\..\..\..\..\src\pyblish-nuke\pyblish_nuke\nuke_path;"

f.write(path)
f.write("\n")

path = r"set HOUDINI_PATH=%HOUDINI_PATH%;"
path += r"%~dp0..\..\..\..\..\..\src\pyblish-houdini\pyblish_houdini"
path += r"\houdini_path;"

f.write(path)
f.write("\n")

f.close()
