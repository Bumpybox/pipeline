import os
import subprocess

# installing flake8
subprocess.call(['pip', 'install', 'flake8'])

# finding all source modules
root = os.path.dirname(os.path.dirname(__file__))
paths = [root]
sources = os.path.join(root, "src")
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
