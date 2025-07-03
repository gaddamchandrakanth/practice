def downloadcode(repo)
{
  git "https://github.com/IntelliqDevops/${repo}.git"
}
def artifact()
{
  sh "mvn package"
}
def deploy(jobname,ip,contextpath)
{
  sh "scp /var/lib/jenkins/workspace/${jobname}/webapp/target/webapp.war ubuntu@${ip}:/var/lib/tomcat10/webapps/${contextpath}.war"
}
def java()
{
  sh "java -jar /var/lib/jenkins/workspace/pipeline/testing.jar"
}

