

pipeline {
  
    stages {


stage("install pip dependencies") {
  agent { 
    docker {
      label "docker && linux" 
      image "python:3.7"
    }
  }
  steps {
    withEnv(["HOME=${env.WORKSPACE}"]) {
      sh "pip install virtualenv"
      sh "virtualenv venv"
      sh "pip install -r requirements.txt "

    }
  }

}

    }}
