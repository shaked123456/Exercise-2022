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
           sh '''curl -v --user admin:Nopass5! --upload-file "{a_1.2.0.zip,b_1.2.0.zip,c_1.2.0.zip,d_1.2.0.zip}" "http://192.168.1.242:8082/artifactory/binary-storage/"'''
       }
 }
}
}
