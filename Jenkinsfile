pipeline {
    agent {
	label "ubuntu"
        docker { image 'ubuntu:v1' }
    }
//    agent {
//        dockerfile {
//        filename 'Dockerfile'
//        }  
//    }
    stages {
	    
	stage('build') {    
            steps {
                sh 'python zip_job.py'
            }
        }

        stage('Upload to Artifactory') {
            steps {
                sh '''jf rt upload --url http://192.168.1.242:8082/artifactory/ --user 'admin' --password 'Nopass5!' '*1.2.0.zip' binary-storage/'''
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
