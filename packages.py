import json
import os
import subprocess

root = os.path.dirname(os.path.dirname(__file__))

data = None
with open(os.path.join(os.path.dirname(__file__), 'packages.json'), "r") as f:
    data = json.loads(f.read())

for package in data:
    package_root = os.path.join(root, package['name'])

    if not os.path.exists(package_root):
        os.makedirs(package_root)
        subprocess.Popen(['git', 'clone', package['repository'], package_root],
                         shell=True)
    else:
        if subprocess.call(["git", "branch"], stderr=subprocess.STDOUT,
                           stdout=open(os.devnull, 'w')) != 0:
            print "%s is not empty and not a git repository." % package_root
        else:
            print "update %s" % package_root
