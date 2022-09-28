pipeline { 
agent none
stages {
    stage('Build Stage') {
        agent {
           dockerfile{
            filename 'Dockerfile'}
        }
        steps {
           echo 'testing stage running'
           sh "ls"
           sh "python3 zip_job.py"
       }
 }
}
}
