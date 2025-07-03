def code(repo)
{
  git "https://github.com/IntelliqDevops/$(repo).git"
}
def build()
{
  sh "mvn package"
}
