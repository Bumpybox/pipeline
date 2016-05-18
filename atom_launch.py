import os
import subprocess

root = os.path.join(os.path.dirname(__file__), "src")
paths = [os.path.dirname(__file__)]
if os.path.exists(root):
    for item in os.listdir(root):
        path = os.path.join(root, item)
        if os.path.isdir(path):
            paths.append(path)

cmd = [os.path.join(os.environ["LOCALAPPDATA"], "atom", "bin", "atom.cmd")]
cmd.extend(paths)

subprocess.Popen(cmd)
