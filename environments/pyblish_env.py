import os
import subprocess
import sys
import argparse


def setup(repo_path=None):

    if not repo_path:
        repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_root = os.path.dirname(sys.executable)

    # install pyblish-base
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-base.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/pyblish/pyblish-base.git" +
                         "#egg=pyblish-base"], cwd=repo_path)

    # install pyblish-lite
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-lite.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-lite\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/pyblish/pyblish-lite.git" +
                         "#egg=pyblish-lite"], cwd=repo_path)

    # install pyblish-nuke
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-nuke.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-nuke\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/pyblish/pyblish-nuke.git" +
                         "#egg=pyblish-nuke"], cwd=repo_path)

    # install pyblish-maya
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-maya.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-maya\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/pyblish/pyblish-maya.git" +
                         "#egg=pyblish-maya"], cwd=repo_path)

    # install pyblish-houdini
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-houdini.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-houdini\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/pyblish/pyblish-houdini.git" +
                         "#egg=pyblish-houdini"], cwd=repo_path)
    """
    # install pyblish-standalone
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-standalone.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-standalone\""
    else:
        subprocess.call(["pip", "install", "--editable", "git+https://" +
                         "github.com/pyblish/pyblish-standalone.git" +
                         "#egg=pyblish-standalone"], cwd=repo_path)
    """
    # setup environment variables
    dst = os.path.join(env_root, "etc", "conda", "activate.d",
                       "pyblish_env.bat")

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    f = open(dst, "w")

    path = r"set PYTHONPATH=%PYTHONPATH%;"
    path += r"%~dp0..\..\..\..\..\..\pythonpath;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-base;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-qml;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-nuke;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-maya;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-standalone;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-maya\pyblish_maya\pythonpath;"
    path += r"%~dp0..\..\..\..\..\..\environments\variables\pyblish_env"
    path += r"\pythonpath;"
    path += r"%~dp0..\..\..\Lib\site-packages;"

    f.write(path)
    f.write("\n")

    path = r"set NUKE_PATH=%NUKE_PATH%;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-nuke\pyblish_nuke\nuke_path;"
    path += r"%~dp0..\..\..\..\..\..\environments\variables\pyblish_env"
    path += r"\nuke_path;"

    f.write(path)
    f.write("\n")

    path = r"set HOUDINI_PATH=%HOUDINI_PATH%;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-houdini\pyblish_houdini"
    path += r"\houdini_path;"
    path += r"%~dp0..\..\..\..\..\..\environments\variables\pyblish_env"
    path += r"\houdini_path;"
    path += r"^&"

    f.write(path)
    f.write("\n")

    f.close()


def launch():

    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pyblish_env")
    parser.add_argument("--setup", dest="setup", action="store_true",
                        help="Setup the environment.")
    parser.add_argument("--launch", dest="launch", action="store_true",
                        help="Launch any required processes.")

    kwargs = parser.parse_args(sys.argv[1:])
    if kwargs.setup:
        setup()

    if kwargs.launch:
        launch()
