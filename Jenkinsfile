pipeline {
   agent any
       stages {


       stage("install pip dependencies") {
      agent { 
        docker {
           label "docker" 
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


    stage("check missing migration ") {
      agent { 
        docker {
           label "docker" 
            image "python:3.7"
           }
           }
       steps {
            script {
            def missing_migration = labelledShell label: 'Run makemigrations command', script: './venv/bin/python manage.py makemigrations --dry-run --noinput --check', returnStatus: true
            if(missing_migration != 0){
            error("Jenkins detect a missing migration file, please double check")
            }
        }
       }

     }


    stage("check codestyle") {
      agent { 
        docker {
           label "docker" 
            image "python:3.7"
           }
           }
       steps {
           script {
            def lint_is_violated = labelledShell label: 'Run flake8 linter', script: './env/bin/flake8', returnStatus: true
            if(lint_is_violated != 0){
                error("Jenkins detect that linting is violated, please fix it")
            }
       }

     }

        stage("check unit test") {
      agent { 
        docker {
           label "docker" 
            image "python:3.7"
           }
           }
       steps {
          withEnv(["HOME=${env.WORKSPACE}"]) {
              labelledShell label: 'Install python coverage', script: './env/bin/pip install coverage'
              labelledShell label: 'Run coverage test', script: './env/bin/coverage run manage.py test'
              labelledShell label: 'Generate coverage xml report', script: './env/bin/coverage xml'
        
         }
       }

     }

     stage("build docker image image ") {
      agent { 
        docker {
           label "docker" 
            image "python:3.7"
           }
           }
       steps {
          echo 'build dokcer file'

         }
       }

     }

}}
