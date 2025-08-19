import subprocess

container_name=input("container name:")
own_port=input("own port:")
port=input("default port:")
image_name=input("image:")

subprocess.call("docker run --name %s -d -p %s:%s %s"%(container_name,own_port,port,image_name),shell=True)


