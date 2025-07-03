def download-code()
{
  git "https://github.com/IntelliqDevops/maven.git"
}
def artifact()
{
  sh "mvn package"
}
