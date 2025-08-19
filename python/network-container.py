import subprocess

i=1
while i<=5:
    subprocess.call("docker network create --driver bridge chandu%d"%i,shell=True)
    subprocess.call("docker run --name n%d -d -P --network chandu%d nginx"%(i,i),shell=True)
    i=i+1
