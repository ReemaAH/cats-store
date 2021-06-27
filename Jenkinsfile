pipeline {
  agent {
    label 'docker-agent'
    
  }
  
  
  
  
  stages {
    stage('install pip dependencies') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh'''
            pip install virtualenv
            virtualenv venv
            pip install -r requirements.txt
          '''
        }
        
        
        
      }
    }
  }
}
