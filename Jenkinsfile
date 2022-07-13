// #!groovy
// properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
        }
//     options {
//         buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
//         timestamps()
//     }
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t web_test ."
                sh "docker run web_test pytest --alluredir='${WORKSPACE}/allure-results' tests/element_test.py"
            }
        stage('reports') {
             steps {
             script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
            }
            }
        }
    }
}
