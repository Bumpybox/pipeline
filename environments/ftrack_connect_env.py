import os
import subprocess
import sys
import platform
import argparse


def setup(repo_path=None):

    if not repo_path:
        repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_root = os.path.dirname(sys.executable)

    # checking repository directory existence
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)

    # install PySide
    src = os.path.join(env_root, "Lib", "site-packages", "PySide")
    if os.path.exists(src):
        print "Skipping existing module: \"PySide\""
    else:
        subprocess.call(["pip", "install", "PySide"])

    # install ftrack-connect
    src = os.path.join(env_root, "Lib", "site-packages",
                       "ftrack-connect.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"ftrack-connect\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://bitbucket.org/ftrack/ftrack-connect" +
                         ".git#egg=ftrack-connect"], cwd=repo_path)

        rcc_exe = os.path.join(env_root, "Lib", "site-packages", "PySide",
                               "pyside-rcc.exe")
        resource_py = os.path.join(repo_path, "src", "ftrack-connect",
                                   "source", "ftrack_connect", "ui",
                                   "resource.py")
        resource_qrc = os.path.join(repo_path, "src", "ftrack-connect",
                                    "resource", "resource.qrc")
        subprocess.call([rcc_exe, "-o", resource_py, resource_qrc])

    # install ftrack-connect-foundry
    src = os.path.join(env_root, "Lib", "site-packages",
                       "ftrack-connect-foundry.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"ftrack-connect-foundry\""
    else:
        subprocess.call(["pip", "install", "--editable", "git+https://" +
                         "bitbucket.org/ftrack/ftrack-connect-foundry.git" +
                         "#egg=ftrack-connect-foundry"], cwd=repo_path)

    # install ftrack-connect-nuke
    src = os.path.join(env_root, "Lib", "site-packages",
                       "ftrack-connect-nuke.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"ftrack-connect-nuke\""
    else:
        subprocess.call(["pip", "install", "--editable", "git+https://" +
                         "bitbucket.org/ftrack/ftrack-connect-nuke.git" +
                         "#egg=ftrack-connect-nuke"], cwd=repo_path)

    # install ftrack-connect-maya
    src = os.path.join(env_root, "Lib", "site-packages",
                       "ftrack-connect-maya.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"ftrack-connect-maya\""
    else:
        subprocess.call(["pip", "install", "--editable", "git+https://" +
                         "bitbucket.org/ftrack/ftrack-connect-maya.git" +
                         "#egg=ftrack-connect-maya"], cwd=repo_path)

    # setup env_nameironment variables
    dst = os.path.join(env_root, "etc", "conda", "activate.d", "env_vars.bat")

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    # check for existing env_nameironment file
    f = None
    if os.path.exists(dst):
        # check of existing env_nameironment setup
        f = open(dst, "r")
        if "REM ftrack-connect\n" in f.read():
            print "Skipping environment variables setup. Found existing setup."
            return

        f = open(dst, "a")
        print "Found existing environment file. Appending to it."
    else:
        f = open(dst, "w")
        print "Creating new environment file."

    f.write("REM ftrack-connect")
    f.write("\n")

    path = r"set PYTHONPATH=%PYTHONPATH%;%~dp0..\..\..\..\..\..\pythonpath;"
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-nuke\source;"
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect\source;"
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-foundry\source;"
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-maya\source;"
    path += r"%~dp0..\..\..\Lib\site-packages"

    f.write(path)
    f.write("\n")

    path = r"set FTRACK_CONNECT_PLUGIN_PATH=%FTRACK_CONNECT_path%;"
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect;"
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-foundry;"
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-nuke;"
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-maya;"
    path += r"%~dp0..\..\..\..\..\..\environments\variables"
    path += r"\ftrack_connect_env\ftrack_connect_plugin_path"

    f.write(path)
    f.write("\n")

    path = r"set FTRACK_CONNECT_NUKE_PLUGINS_PATH="
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-nuke\resource"

    f.write(path)
    f.write("\n")

    path = r"set FTRACK_CONNECT_MAYA_PLUGINS_PATH="
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-connect-maya\resource"

    f.write(path)
    f.write("\n")


def launch():

    # launching ftrack-connect without a console window
    kwargs = {}
    """
    if platform.system() == 'Windows':
        CREATE_NEW_PROCESS_GROUP = 0x00000200
        DETACHED_PROCESS = 0x00000008
        kwargs.update(creationflags=DETACHED_PROCESS |
                      CREATE_NEW_PROCESS_GROUP)
    elif sys.version_info < (3, 2):  # assume posix
        kwargs.update(preexec_fn=os.setsid)
    else:  # Python 3.2+ and Unix
        kwargs.update(start_new_session=True)
    """
    subprocess.call(["python", "-m", "ftrack_connect"], **kwargs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ftrack_connect_env")
    parser.add_argument("--setup", dest="setup", action="store_true",
                        help="Setup the environment.")
    parser.add_argument("--launch", dest="launch", action="store_true",
                        help="Launch any required processes.")

    kwargs = parser.parse_args(sys.argv[1:])
    if kwargs.setup:
        setup()

    if kwargs.launch:
        launch()
