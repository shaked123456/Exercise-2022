pipeline {
    agent {
    // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
        dockerfile {
            filename 'Dockerfile'
            dir 'build'
            label 'my-defined-label'
        }
    }	    
    stages {
	    stage('build') {
            steps {
                sh 'python zip_job.py'
            }
        }
    }
	
    post {
        // Clean after build
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
