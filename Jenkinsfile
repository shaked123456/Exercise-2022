pipeline {	
    agent {
        dockerfile{
	     filename 'Dockerfile'
             args '--privileged --add-host artifactory-tlv:192.168.1.242'
	     label 'zip-job-docker'}
        }
    stages {	    
	stage('Build Stage') {    
            steps {
                sh 'python3 zip_job.py'
            }
         }

        stage('Upload zip files to Artifactory') {
            steps {
                sh '''curl -v --user admin:Nopass5! --upload-file "{a_1.2.0.zip,b_1.2.0.zip,c_1.2.0.zip,d_1.2.0.zip}" "http://artifactory-tlv:8082/artifactory/binary-storage/$VERSION/"'''
            }
        }	    
}
    post {
        always {
	    mail to: "shaked@wizards.co.il",
            subject: "Test Email",
            body: '${env.BUILD_STATUS}'
        }	
}
}	
