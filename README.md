🙏 Hanuman Kripa ❤️

This project demonstrates a complete CI/CD pipeline using Jenkins and SonarQube, triggered automatically via GitHub Webhook. The pipeline performs static code analysis and enforces Quality Gates to fail or pass builds based on code quality.

⸻

📌 Project Overview
	•	GitHub → Jenkins (Webhook trigger)
	•	Jenkins → SonarQube (Code Analysis)
	•	SonarQube → Jenkins (Quality Gate via Webhook)

Whenever code is pushed to the main branch:
	1.	GitHub triggers Jenkins automatically
	2.	Jenkins pulls the code
	3.	SonarQube analyzes the code
	4.	Jenkins waits for Quality Gate result
	5.	Build FAILS or PASSES based on rules

⸻

🧱 Tech Stack
	•	Jenkins
	•	SonarQube (Community Edition)
	•	GitHub Webhooks
	•	Python (Sample code)
	•	Docker (for SonarQube setup)

⸻

📂 Repository Structure

jenkins-sonarqube-cicd/
│── app/
│   └── main.py
│── Jenkinsfile
│── docker-compose.yml
│── sonar-project.properties
│── README.md


⸻

🧪 Sample Code Used

❌ Insecure Code (Fails Quality Gate)

def insecure_login():
    password = "admin123"  # hardcoded password
    while True:
        pass

Issues detected:
	•	Hardcoded password
	•	Infinite loop
	•	Security hotspot

⸻

✅ Secure Code (Passes Quality Gate)

def secure_login(password):
    if not password:
        raise ValueError("Password required")
    return True


⸻

⚙️ Jenkinsfile (Pipeline)

pipeline {
    agent any

    tools {
        sonarQubeScanner 'SonarScanner'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/iamdeepaktiwari08/jenkins-sonarqube-cicd.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 15, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}


⸻

🔗 Webhook Configuration

GitHub → Jenkins

Payload URL

http://<JENKINS-IP>:8080/github-webhook/

	•	Content type: application/json
	•	Event: Push

⸻

SonarQube → Jenkins (Quality Gate)

Webhook URL

http://<JENKINS-IP>:8080/sonarqube-webhook/

Used to notify Jenkins when analysis is complete.

⸻

📊 Quality Gate Rules Used
	•	Coverage < 80% → FAIL
	•	Bugs > 0 → FAIL
	•	Vulnerabilities > 0 → FAIL
	•	Security Hotspots Reviewed < 100% → FAIL

⸻

✅ Final Result
	•	❌ Insecure code → Pipeline FAILED
	•	✅ Secure code → Pipeline PASSED
	•	🚀 Webhook successfully triggers Jenkins automatically

⸻

🎯 What You Learn From This Project
	•	End-to-end CI/CD pipeline
	•	Jenkins + SonarQube integration
	•	Quality Gates in real-time
	•	GitHub Webhook automation
	•	DevSecOps fundamentals

⸻

👨‍💻 Author

Deepak Tiwari
Cloud & DevOps Engineer (Fresher)

⸻

⭐ If you like this project, give it a star on GitHub!
