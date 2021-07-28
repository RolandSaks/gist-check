
pipeline { 
    environment { 
        registry = "testgistpipe" 
        registryCredential = 'dockerhub' 
        dockerImage = '' 

    }

    agent any 
    stages { 

        stage('checkout') { 
            steps { 
                script{
                    git branch: 'main', credentialsId: 'github', url: 'https://github.com/RolandSaks/gist-check'
                }
            }
        } 
        stage('Building our image') { 

            steps { 
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            } 
        }

        stage('Deploy our image') { 
            steps { 
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                } 
            }
        } 

        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $registry:$BUILD_NUMBER" 
            }
        } 
    }
}
