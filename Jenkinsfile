@Library('cve-scan') _

pipeline {
  agent { label 'build' }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build and test') {
      steps {
        sh '''
          docker run --rm -u $(id -u):$(id -g) -e HOME=/tmp -v "$PWD":/app -w /app \
            python:3.12-slim sh -c "pip install --user -r requirements.txt && python manage.py test"
        '''
      }
    }
    stage('Dependency scan') { steps { script { cveScan.scan() } } }
    stage('CVE evaluate')    { steps { script { cveScan.evaluate(projectName: 'demo-django', threshold: 7.0) } } }
  }
}