def download(repo)
{
  git "https://github.com/IntelliqDevops/${repo}.git"
}
def artifact()
{
  sh "mvn package"
}
def deployartifact(jobname,ip,contextpath)

  
