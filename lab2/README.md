# MLOps homework #2

Team #2

Jenkins pipeline script to train ML model

* Шершнев Андрей (РИМ-120907)
* Кожин Артём (РИМ-120906)
* Иванов Сергей (РИМ-120906)
* Чупахин Юрий (РИМ-120908)

Script:
```
pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/DenkingOfficial/mlops_hw_1.git'
            }
        }
        stage('Downloading data') {
            steps { 
                sh 'python data_creation.py'
            }
        }
        stage('Data preparation') {
            steps {
                sh 'python model_preprocessing.py'
            }
        }
        stage('Model training') {
            steps {
                sh 'python model_preparation.py'
            }
        }
        stage('Model testing') {
            steps {
                sh 'python model_testing.py'
            }
        }
    }
}
```
