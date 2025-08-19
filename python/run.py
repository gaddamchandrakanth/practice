import subprocess


image_name=input("enter the image name for image:")

image=input("enter the image name to be downloaded:")

subprocess.call("docker run --name %s -d -P %s" %(image_name,image),shell=True)


