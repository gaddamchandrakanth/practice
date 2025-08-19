import subprocess

image=input("enter the image to be downloaded:")

subprocess.call("docker pull %s"%image,shell=True)

