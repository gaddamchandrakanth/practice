def download-code(repo)
{
  git "https://github.com/IntelliqDevops/$(repo).git"
}
def artifact()
{
  sh "mvn package"
}
