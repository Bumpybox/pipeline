import os


environments = []
path = os.path.join(os.path.dirname(__file__), 'environments')
count = 0
for f in os.listdir(path):
    if f.endswith(".bat") and f != 'conda_env.bat':
        environments.append(f)
        print '[%s] - %s' % (str(count), os.path.splitext(f)[0])
