import subprocess

image=input("enter the container name to be deleted:")

subprocess.call("docker rm -f %s"%(image),shell=True)

