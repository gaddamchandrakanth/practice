import subprocess
subprocess.call("docker rm -f $(docker container ls | grep tomcat | awk '{print $1}')",shell=True)
