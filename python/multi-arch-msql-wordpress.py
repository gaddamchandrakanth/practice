import subprocess

subprocess.call("docker network create --driver bridge chandu",shell=True)
subprocess.call("docker run --name database -d -e MYSQL_ROOT_PASSWORD=CHANDU -e MYSQL_USER=CHANDU --network chandu mysql",shell=True)
subprocess.call("docker run --name word-press -d -p 8080:80 --network chandu wordpress",shell=True)

