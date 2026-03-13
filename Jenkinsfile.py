pipeline {
  agent any
  stages {
      stage('Compile java Program'){
         steps {
             bat 'javac HelloWorld.java'
         }
}
}
}
