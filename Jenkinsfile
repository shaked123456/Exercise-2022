pipeline {	
    agent none
    stages {	    
	stage('Build Stage') {    
            steps {
                agent {
                dockerfile{
		filename 'Dockerfile'
		args '--privileged'
	 	label 'zip-job-docker'}
		}
                sh 'python3 zip_job.py'
            }
         }

        stage('Upload zip files to Artifactory') {
            steps {
                sh '''curl -v --user admin:Nopass5! --upload-file "{a_1.2.0.zip,b_1.2.0.zip,c_1.2.0.zip,d_1.2.0.zip}" "http://192.168.1.242:8082/artifactory/binary-storage/"'''
            }
        }	    
}
}    
