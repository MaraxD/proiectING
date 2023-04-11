import subprocess
import sys
import argparse

parser=argparse.ArgumentParser()
cmdType=sys.argv[1]

if cmdType=='build':
    parser.add_argument('build',type=str)
    parser.add_argument('--dockerFilePath',type=str)
    parser.add_argument('--imageName',type=str)
    parser.add_argument('--imageTag',type=str)
    args=parser.parse_args()
    
    command=subprocess.run(["docker",args.build,"-t","{imageName}:{imageTag}".format(imageName=args.imageName,imageTag=args.imageTag),args.dockerFilePath])
    # print(command) for testing only
elif cmdType=='push':
    parser.add_argument('push',type=str)
    parser.add_argument('--username',type=str)
    parser.add_argument('--imageName',type=str)
    parser.add_argument('--imageTag',type=str)
    args=parser.parse_args()

    command=subprocess.run(["docker","image","tag",args.imageName,"{username}/{imageName}:{imageTag}".format(username=args.username,imageName=args.imageName,imageTag=args.imageTag)])
    # print(command)
    command=subprocess.run(["docker","image","push","{username}/{imageName}:{imageTag}".format(username=args.username,imageName=args.imageName,imageTag=args.imageTag)])
    # print(command)
elif cmdType=='deploy':
    #using the image deployed in the public registry
    parser.add_argument('deploy',type=str)
    parser.add_argument('--imageName',type=str)
    parser.add_argument('--imageTag',type=str)
    args=parser.parse_args()

    command=subprocess.run(["docker","container","run","-p","5000:5000","-d","{imageName}:{imageTag}".format(imageName=args.imageName,imageTag=args.imageTag)])
    # print(command)
elif cmdType=='test':
    parser.add_argument('test',type=str)
    parser.add_argument('--endpoint',type=str)
    args=parser.parse_args()
    command=subprocess.run(["curl","-v",args.endpoint])
    # print(command) 
elif cmdType=='deployK':
    parser.add_argument('deployK',type=str)
    parser.add_argument('--deploymentFile',type=str)
    parser.add_argument('--serviceName',type=str)
    args=parser.parse_args()

    command=subprocess.run(["minikube","start"])
    if command.returncode==0:
        command=subprocess.run(["kubectl","apply","-f",args.deploymentFile])
        #problema aici: nu se deschide din prima, isi da refresh si merge
        command=subprocess.run(["minikube","service",args.serviceName,"-n","default"])
