pipeline {
	
    agent {
	docker {
	    label "zip-job-docker"
            image 'zip-job-docker:v1' 
	    args '-v /var/run/docker.sock:/var/run/docker.sock'}
    }
    stages {
	    
	stage('build') {    
            steps {
                sh 'python3 zip_job.py'
            }
        }

        stage('Upload to Artifactory') {
            steps {
                sh '''curl -v --user admin:Nopass5! --upload-file "{a_1.2.0.zip,b_1.2.0.zip,c_1.2.0.zip,d_1.2.0.zip}" "http://192.168.1.242:8082/artifactory/binary-storage/"'''
            }
       }	    
    }	
	
    post {
        always {
            cleanWs(cleanWhenAborted: true,
            cleanWhenFailure: true,
            cleanWhenNotBuilt: false,
            cleanWhenSuccess: true,
            cleanWhenUnstable: true,
            deleteDirs: true,
            notFailBuild: true,
            disableDeferredWipeout: true)
        }
	failure {
	    mail to: 'shaked@wizards.co.il',
	    subject: 'Failed Pipeline: ${currentBuild.fullDisplayName}',
            body: 'Something went wrong with ${env.BUILD_URL}'
	}
	success {
	    mail to: 'shaked@wizards.co.il',
            subject: 'Succeeded Pipeline: ${currentBuild.fullDisplayName}',
	    body: 'Pipeline Succeeded: ${env.BUILD_URL}'
	}		
    }
}
