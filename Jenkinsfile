#!groovy
properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
        }
    option {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t web_test ."
                sh "docker run web_test pytest -s -v tests/"
            }
        }
    }
}
