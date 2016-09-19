import os
import subprocess
import sys
import argparse


def setup(repo_path=None):

    # if no repository path is specified,
    # default to parent directory of pipeline repository
    if not repo_path:
        func = os.path.dirname
        repo_path = func(func(func(os.path.abspath(__file__))))
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
                         ".git@0.1.27#egg=ftrack-connect"], cwd=repo_path)

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
                         "@0.2.3#egg=ftrack-connect-maya"], cwd=repo_path)

    # setup environment variables
    dst = os.path.join(env_root, "etc", "conda", "activate.d",
                       "ftrack_connect_env.bat")

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    f = open(dst, "w")

    path = r"set PYTHONPATH=%PYTHONPATH%;"
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path += os.path.join(root, "pythonpath") + ";"
    path += os.path.join(repo_path, "src", "ftrack-connect", "source") + ";"
    path += os.path.join(repo_path, "src", "ftrack-connect-nuke",
                         "source") + ";"
    path += os.path.join(repo_path, "src", "ftrack-connect-foundry",
                         "source") + ";"
    path += os.path.join(repo_path, "src", "ftrack-connect-maya",
                         "source") + ";"
    path += os.path.join(repo_path, "src", "ftrack-connect-maya",
                         "resource", "scripts") + ";"
    path += os.path.join(env_root, "Lib", "site-packages") + ";"

    f.write(path)
    f.write("\n")

    path = r"set FTRACK_CONNECT_PLUGIN_PATH=%FTRACK_CONNECT_path%;"
    path += os.path.join(repo_path, "src", "ftrack-connect") + ";"
    path += os.path.join(repo_path, "src", "ftrack-connect-nuke") + ";"
    path += os.path.join(repo_path, "src", "ftrack-connect-foundry") + ";"
    path += os.path.join(repo_path, "src", "ftrack-connect-maya") + ";"
    path += os.path.join(root, "environments", "variables",
                         "ftrack_connect_env",
                         "ftrack_connect_plugin_path") + ";"

    f.write(path)
    f.write("\n")

    path = r"set FTRACK_CONNECT_NUKE_PLUGINS_PATH="
    path += os.path.join(repo_path, "src", "ftrack-connect-nuke",
                         "resource")

    f.write(path)
    f.write("\n")

    path = r"set FTRACK_CONNECT_MAYA_PLUGINS_PATH="
    path += os.path.join(repo_path, "src", "ftrack-connect-maya",
                         "resource")

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
