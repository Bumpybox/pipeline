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

    # install ftrack-hooks
    src = os.path.join(env_root, "Lib", "site-packages",
                       "ftrack-hooks.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"ftrack-hooks\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://github.com/tokejepsen/ftrack-hooks.git" +
                         "#egg=ftrack-hooks"], cwd=repo_path)

    # install pyblish-bumpybox
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pyblish-bumpybox.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pyblish-bumpybox\""
    else:
        subprocess.call(["pip", "install", "--editable", "git+" +
                         "https://github.com/Bumpybox/pyblish-bumpybox.git" +
                         "#egg=pyblish-bumpybox"], cwd=repo_path)

    # install pipeline-schema
    src = os.path.join(env_root, "Lib", "site-packages",
                       "pipeline-schema.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"pipeline-schema\""
    else:
        subprocess.call(["pip", "install", "--editable", "git+" +
                         "https://github.com/Bumpybox/pipeline-schema.git" +
                         "#egg=pipeline-schema"], cwd=repo_path)

    # install lucidity
    src = os.path.join(env_root, "Lib", "site-packages",
                       "lucidity.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"lucidity\""
    else:
        subprocess.call(["pip", "install", "--editable",
                         "git+https://gitlab.com/4degrees/lucidity.git" +
                         "#egg=lucidity"], cwd=repo_path)

    # setup environment variables
    dst = os.path.join(env_root, "etc", "conda", "activate.d",
                       "pipeline_env.bat")

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    f = open(dst, "w")

    path = r"set FTRACK_CONNECT_PLUGIN_PATH=%FTRACK_CONNECT_PLUGIN_PATH%;"
    path += os.path.join(repo_path, "src", "ftrack-hooks") + ";"

    f.write(path)
    f.write("\n")

    path = r"set PYTHONPATH=%PYTHONPATH%;"
    path += os.path.join(repo_path, "src", "pyblish-bumpybox") + ";"
    path += os.path.join(repo_path, "src", "pyblish-bumpybox",
                         "pyblish_bumpybox", "environment_variables",
                         "pythonpath") + ";"
    path += os.path.join(repo_path, "src", "pipeline-schema") + ";"
    path += os.path.join(repo_path, "src", "lucidity", "source") + ";"

    f.write(path)
    f.write("\n")

    path = r"set NUKE_PATH=%NUKE_PATH%;"
    path += os.path.join(repo_path, "src", "pyblish-bumpybox",
                         "pyblish_bumpybox", "environment_variables",
                         "nuke_path") + ";"

    f.write(path)
    f.write("\n")

    path = r"set HIERO_PLUGIN_PATH=%HIERO_PLUGIN_PATH%;"
    path += os.path.join(repo_path, "src", "pyblish-bumpybox",
                         "pyblish_bumpybox", "environment_variables",
                         "hiero_plugin_path") + ";"

    f.write(path)
    f.write("\n")

    path = r"set HOUDINI_PATH=%HOUDINI_PATH%;"
    path += os.path.join(repo_path, "src", "pyblish-bumpybox",
                         "pyblish_bumpybox", "environment_variables",
                         "houdini_path") + ";^&"

    f.write(path)
    f.write("\n")

    f.close()


def launch():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pipeline_env")
    parser.add_argument("--setup", dest="setup", action="store_true",
                        help="Setup the environment.")
    parser.add_argument("--launch", dest="launch", action="store_true",
                        help="Launch any required processes.")

    kwargs = parser.parse_args(sys.argv[1:])
    if kwargs.setup:
        setup()

    if kwargs.launch:
        launch()
