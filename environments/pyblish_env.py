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

    # install pyblish-standalone
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-standalone.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-standalone\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/tokejepsen/" +
                         "pyblish-standalone.git#egg=pyblish-standalone"],
                        cwd=repo_path)

    # install pyblish-aftereffects
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-aftereffects.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-aftereffects\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/tokejepsen/" +
                         "pyblish-aftereffects.git#egg=pyblish-aftereffects"],
                        cwd=repo_path)

    # install pyblish-ftrack
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-ftrack.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-ftrack\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/tokejepsen/" +
                         "pyblish-ftrack.git#egg=pyblish-ftrack"],
                        cwd=repo_path)

    # install pyblish-deadline
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-deadline.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-deadline\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/tokejepsen/" +
                         "pyblish-deadline.git#egg=pyblish-deadline"],
                        cwd=repo_path)

    # setup environment variables
    dst = os.path.join(env_root, "etc", "conda", "activate.d",
                       "pyblish_env.bat")

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    f = open(dst, "w")

    path = r"set PYTHONPATH=%PYTHONPATH%;"
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path += os.path.join(root, "pythonpath") + ";"
    path += os.path.join(repo_path, "src", "pyblish-base") + ";"
    path += os.path.join(repo_path, "src", "pyblish-lite") + ";"
    path += os.path.join(repo_path, "src", "pyblish-nuke") + ";"
    path += os.path.join(repo_path, "src", "pyblish-maya") + ";"
    path += os.path.join(repo_path, "src", "pyblish-houdini") + ";"
    path += os.path.join(repo_path, "src", "pyblish-standalone") + ";"
    path += os.path.join(repo_path, "src", "pyblish-aftereffects") + ";"
    path += os.path.join(repo_path, "src", "pyblish-ftrack") + ";"
    path += os.path.join(repo_path, "src", "pyblish-deadline") + ";"
    path += os.path.join(repo_path, "src", "pyblish-maya", "pyblish_maya",
                         "pythonpath") + ";"
    path += os.path.join(root, "environments", "variables", "pyblish_env",
                         "pythonpath") + ";"
    path += os.path.join(env_root, "Lib", "site-packages") + ";"

    f.write(path)
    f.write("\n")

    path = r"set NUKE_PATH=%NUKE_PATH%;"
    path += os.path.join(repo_path, "src", "pyblish-nuke", "pyblish_nuke",
                         "nuke_path") + ";"
    path += os.path.join(root, "environments", "variables", "pyblish_env",
                         "nuke_path") + ";"

    f.write(path)
    f.write("\n")

    path = r"set HOUDINI_PATH=%HOUDINI_PATH%;"
    path += os.path.join(repo_path, "src", "pyblish-houdini",
                         "pyblish_houdini", "houdini_path") + ";"
    path += os.path.join(root, "environments", "variables", "pyblish_env",
                         "houdini_path") + ";"

    f.write(path)
    f.write("\n")

    f.close()

    # houdini path needs special treatment to force ^& to be at the end of
    # the environment variable
    dst = os.path.join(env_root, "etc", "conda", "activate.d",
                       "z_houdini.bat")

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    f = open(dst, "w")
    path = r"set HOUDINI_PATH=%HOUDINI_PATH%;^&"
    f.write(path)
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
