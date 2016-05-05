import json
import os
import subprocess

root = os.path.join(os.path.dirname(__file__), 'repositories')

data = None
with open(os.path.join(os.path.dirname(__file__), 'repositories.json'), "r") as f:
    data = json.loads(f.read())

for package in data:
    package_root = os.path.join(root, package['name'])

    if not os.path.exists(package_root):
        os.makedirs(package_root)
        subprocess.call(['git', 'clone', package['repository'], package_root],
                        shell=True)
    else:
        if subprocess.call(["git", "branch"], stderr=subprocess.STDOUT,
                           stdout=open(os.devnull, 'w')) != 0:
            print "%s is not empty and not a git repository." % package_root
        else:
            print package['name']
            subprocess.call(['git', '-C', package_root, 'pull'],
                            shell=True)

os.system('pause')
