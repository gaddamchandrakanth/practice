import subprocess

i=1
while i<=3:
    subprocess.call("docker network create --driver bridge tomcat%d"%i,shell=True)
    subprocess.call("docker run --name t%d -d -P --network tomcat%d tomcat"%(i,i),shell=True)
    i=i+1

