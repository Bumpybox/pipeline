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

    # install PyQt5 not in developer mode
    src = os.path.join(env_root, "Lib", "site-packages",
                       "PyQt5")
    if os.path.exists(src):
        print "Skipping existing module: \"PyQt5\""
    else:
        subprocess.call(["pip", "install",
                         "git+https://github.com/pyqt/python-qt5.git"],
                        cwd=repo_path)

    # install pyblish-qml
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-qml.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-qml\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/pyblish/pyblish-qml.git" +
                         "#egg=pyblish-qml"], cwd=repo_path)

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
    dst = os.path.join(env_root, "etc", "conda", "activate.d", "env_vars.bat")

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    # check for existing environment file
    f = None
    if os.path.exists(dst):
        # check of existing environment setup
        f = open(dst, "r")
        if "REM pyblish\n" in f.read():
            return

        f = open(dst, "a")
    else:
        f = open(dst, "w")

    f.write("REM pyblish")
    f.write("\n")

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


def launch():

    # launching pyblish-qml without a console window
    subprocess.call(["python", "-m", "pyblish_qml"])

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
