pipeline {
 stages {
    stage('Build Stage') {
        agent {
           dockerfile{
           filename 'Dockerfile'
        }
        steps {
           echo 'testing stage running'
           sh "ls"
       }
 }
}    
