import json
import os
import subprocess

data = None
with open(os.path.join(os.path.dirname(__file__), 'packages.json'), "r") as f:
    data = json.loads(f.read())

root = os.path.dirname(os.path.dirname(__file__))

for package in data:
    package_root = os.path.join(root, package['name'])
    if not os.path.exists(package_root):
        os.makedirs(package_root)

    subprocess.Popen(['git', 'clone', package['repository'], package_root],
                     shell=True)
