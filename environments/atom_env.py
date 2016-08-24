import os
import subprocess
import sys
import argparse


def setup():

    env_root = os.path.dirname(sys.executable)

    # install ftrack-hooks
    src = os.path.join(env_root, "Lib", "site-packages",
                       "flake8.egg-link")
    if os.path.exists(src):
        print "Skipping existing module: \"flake8\""
    else:
        subprocess.call(["pip", "install", "flake8"])


def launch():

    # finding all source modules
    # default to parent directory of pipeline repository
    func = os.path.dirname
    root = func(func(os.path.abspath(__file__)))
    paths = [root]
    sources = os.path.join(func(root), "src")
    if os.path.exists(sources):
        for item in os.listdir(sources):
            path = os.path.join(sources, item)
            if os.path.isdir(path):
                paths.append(path)

    # finding atom executable
    matches = []
    path = os.path.join(os.environ["LOCALAPPDATA"], "atom")
    for sources, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename == "atom.exe":
                matches.append(os.path.join(sources, filename))
    matches.sort()

    cmd = [matches[-1]]
    cmd.extend(paths)

    subprocess.Popen(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="atom_env")
    parser.add_argument("--setup", dest="setup", action="store_true",
                        help="Setup the environment.")
    parser.add_argument("--launch", dest="launch", action="store_true",
                        help="Launch any required processes.")

    kwargs = parser.parse_args(sys.argv[1:])
    if kwargs.setup:
        setup()

    if kwargs.launch:
        launch()
