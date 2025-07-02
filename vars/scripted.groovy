def Download(repo)
{
  git "https://github.com/IntelliqDevops/${repo}.git"
}
def build()
{
  sh "mvn package"
}
def deploymentartifact(jobname,ip,contextpath)
{
  sh "scp /var/lib/jenkins/workspace/${jobname}/webapp/target/webapp.war ubuntu@${ip}:/var/lib/tomcat10/webapps/${contextpath}.war"
}
  
