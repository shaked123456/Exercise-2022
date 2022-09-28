pipeline {
    agent any
//        dockerfile {
//        filename 'Dockerfile'
//        }  
//  }
    stages {
	    
	stage('build') {    
            steps {
                sh 'python zip_job.py'
            }
        }
	    
        stage('Artifactory download and upload'){
            steps {
                script{
                    // Obtain an Artifactory server instance, defined in Jenkins --> Manage:
                    def server = Artifactory.server SERVER_ID

                    // Read the download and upload specs:
                    def uploadSpec = readFile '/tmp/zip_job.py'

                    // Upload files to Artifactory:
                    def buildInfo = server.upload spec: uploadSpec

                    // Publish build-info to Artifactory
                    server.publishBuildInfo buildInfo
                }
	    }
	}
        stage('Upload to Artifactory') {
            steps {
                sh '''jf rt upload --url http://192.168.1.242:8082/artifactory/ --user 'admin' --password 'Nopass5!' a_1.2.0.zip binary-storage/'''
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
