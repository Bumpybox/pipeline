import os
import subprocess

# finding all source modules
root = os.path.join(os.path.dirname(__file__), "src")
paths = [os.path.dirname(__file__)]
if os.path.exists(root):
    for item in os.listdir(root):
        path = os.path.join(root, item)
        if os.path.isdir(path):
            paths.append(path)

# finding atom executable
matches = []
path = os.path.join(os.environ["LOCALAPPDATA"], "atom")
for root, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename == "atom.exe":
            matches.append(os.path.join(root, filename))
matches.sort()

cmd = [matches[-1]]
cmd.extend(paths)

subprocess.Popen(cmd)
