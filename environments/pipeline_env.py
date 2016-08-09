import os
import subprocess
import sys
import argparse


def setup(repo_path=None):

    if not repo_path:
        repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_root = os.path.dirname(sys.executable)

    # install ftrack-hooks
    subprocess.call(["pip", "install", "--editable",
                     "git+https://github.com/tokejepsen/ftrack-hooks.git" +
                     "#egg=ftrack-hooks"], cwd=repo_path)

    # install pyblish-bumpybox
    subprocess.call(["pip", "install", "--editable",
                     "git+https://github.com/Bumpybox/pyblish-bumpybox.git" +
                     "#egg=pyblish-bumpybox"], cwd=repo_path)

    # install pyblish-bumpybox
    subprocess.call(["pip", "install", "--editable",
                     "git+https://github.com/Bumpybox/pipeline-schema.git" +
                     "#egg=pipeline-schema"], cwd=repo_path)

    # install pyblish-bumpybox
    subprocess.call(["pip", "install", "--editable",
                     "git+https://gitlab.com/4degrees/lucidity.git" +
                     "#egg=lucidity"], cwd=repo_path)

    # setup environment variables
    dst = os.path.join(env_root, "etc", "conda", "activate.d",
                       "env_vars.bat")

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    # check for existing environment file
    f = None
    if os.path.exists(dst):
        # check of existing environment setup
        f = open(dst, "r")
        if "REM pipeline\n" in f.read():
            return

        f = open(dst, "a")
    else:
        f = open(dst, "w")

    f.write("REM pipeline")
    f.write("\n")

    path = r"set FTRACK_EVENT_PLUGIN_PATH=%FTRACK_EVENT_PLUGIN_PATH%;"
    path += r"%~dp0..\..\..\..\..\..\src\ftrack-hooks;"

    f.write(path)
    f.write("\n")

    path = r"set PYTHONPATH=%PYTHONPATH%;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-bumpybox;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-bumpybox\pyblish_bumpybox;"
    path += r"%~dp0..\..\..\..\..\..\src\pipeline-schema;"
    path += r"%~dp0..\..\..\..\..\..\src\lucidity\source"
    path += r"\pythonpath;"

    f.write(path)
    f.write("\n")

    path = r"set NUKE_PATH=%NUKE_PATH%;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-bumpybox\pyblish_bumpybox"
    path += r"\nuke_path;"

    f.write(path)
    f.write("\n")

    path = r"set HIERO_PLUGIN_PATH=%HIERO_PLUGIN_PATH%;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-bumpybox\pyblish_bumpybox"
    path += r"\hiero_plugin_path;"

    f.write(path)
    f.write("\n")

    path = r"set HOUDINI_PATH=%HOUDINI_PATH%;"
    path += r"%~dp0..\..\..\..\..\..\src\pyblish-bumpybox\pyblish_bumpybox"
    path += r"\houdini_path;^&"

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
