import subprocess
import sys

type=sys.argv[1]


if type=='build':
    list_ceva=subprocess.run(["docker","build","-t","flask-app2",sys.argv[2]])
    print(list_ceva)
elif type=='curl':
    list_ceva=subprocess.run(["curl",sys.argv[2]])
    print(list_ceva) 
elif type=='deploy':
    list_ceva=subprocess.run(["docker","container","run","-p","5000:5000",sys.argv[2]])
    print(list_ceva)
