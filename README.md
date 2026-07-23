# 🚀 AWS DevOps CI/CD Project

A complete end-to-end DevOps portfolio project demonstrating modern software delivery using **Python, Flask, Docker, GitHub, AWS EC2, GitHub Actions, Terraform, and Ansible**.

This project demonstrates the complete software development lifecycle—from local development to cloud deployment using modern DevOps practices.

---

# 📌 Project Overview

This project showcases how a Python Flask application can be:

- Developed locally
- Version controlled using Git
- Hosted on GitHub
- Containerized using Docker
- Deployed to AWS EC2
- Automated using GitHub Actions
- Managed using Infrastructure as Code

The goal is to simulate a real-world DevOps workflow that is commonly used in production environments.

---

# 🏗️ Architecture

```
                 Developer
                     │
             VS Code + Git
                     │
                GitHub Repository
                     │
            GitHub Actions (CI/CD)
                     │
               Docker Image Build
                     │
                AWS EC2 Instance
                     │
              Docker Container
                     │
             Gunicorn Web Server
                     │
             Flask Web Application
```

---

# 🛠 Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Framework | Flask |
| Web Server | Gunicorn |
| Containerization | Docker |
| Version Control | Git |
| Repository | GitHub |
| Cloud | AWS EC2 |
| Operating System | Ubuntu Linux |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Infrastructure | Terraform *(Upcoming)* |
| Configuration | Ansible *(Upcoming)* |

---

# 📂 Project Structure

```
aws-devops-cicd-project/
│
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   └── app.py
│
├── tests/
│   ├── __init__.py
│   └── test_app.py
│
├── .github/
│   └── workflows/
│
├── Dockerfile
├── requirements.txt
├── run.py
├── README.md
├── .gitignore
└── .dockerignore
```

---

# ✨ Features

- Flask web application
- Health check endpoint
- Docker containerization
- AWS EC2 deployment
- Gunicorn production server
- Unit testing using Pytest
- Linux server management
- Git version control
- GitHub repository
- Ready for CI/CD automation

---

# 🚀 Local Setup

## Clone Repository

```bash
git clone https://github.com/sreepradat/aws-devops-cicd-project.git

cd aws-devops-cicd-project
```

## Create Virtual Environment (Windows)

```powershell
python -m venv .venv

.\.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python run.py
```

Application URL:

```
http://localhost:5000
```

Health Endpoint:

```
http://localhost:5000/health
```

---

# 🧪 Run Tests

```bash
pytest -v
```

---

# 🐳 Docker

## Build Docker Image

```bash
docker build -t flask-app .
```

## Run Docker Container

```bash
docker run -d -p 5000:5000 --name flask-container flask-app
```

## View Running Containers

```bash
docker ps
```

## View Docker Images

```bash
docker images
```

## View Container Logs

```bash
docker logs flask-container
```

## Stop Container

```bash
docker stop flask-container
```

## Start Container

```bash
docker start flask-container
```

## Restart Container

```bash
docker restart flask-container
```

---

# ☁️ AWS EC2 Deployment

The application has been successfully deployed on an Ubuntu EC2 instance hosted on AWS.

Deployment steps completed:

- Created AWS account
- Configured IAM user
- Launched Ubuntu EC2 instance
- Configured Security Groups
- Connected using SSH
- Installed Docker
- Cloned GitHub repository
- Built Docker image
- Started Docker container
- Verified application
- Configured Docker restart policy

---

## Application URL

```
http://18.236.187.63:5000
```

## Health Check

```
http://18.236.187.63:5000/health
```

---

# 🔄 Deployment Workflow

```
Developer
    │
    ▼
VS Code
    │
    ▼
Git Commit
    │
    ▼
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ▼
AWS EC2
    │
    ▼
Docker
    │
    ▼
Flask Application
```

---

# 📊 Current Progress

## Completed

- ✅ AWS Account
- ✅ IAM User
- ✅ Git Installation
- ✅ GitHub Repository
- ✅ VS Code Setup
- ✅ Python Virtual Environment
- ✅ Flask Application
- ✅ HTML Frontend
- ✅ Health Check API
- ✅ Unit Testing using Pytest
- ✅ Docker Containerization
- ✅ AWS EC2 Deployment
- ✅ Ubuntu Linux Administration
- ✅ SSH Connectivity
- ✅ Gunicorn Production Server
- ✅ Docker Restart Policy

## In Progress

- GitHub Actions CI

## Upcoming

- Continuous Deployment
- Terraform
- Ansible
- Nginx
- Monitoring
- CloudWatch
- Prometheus
- Grafana

---

# 💼 Skills Demonstrated

- Python
- Flask
- Docker
- Git
- GitHub
- Linux
- AWS EC2
- Ubuntu
- SSH
- Gunicorn
- DevOps
- CI/CD
- Infrastructure as Code

---

# 📸 Screenshots

You can add screenshots of the following:

- Home Page
- Health Endpoint
- Docker Running Container
- EC2 Instance
- GitHub Repository
- GitHub Actions Workflow (after CI is completed)

Example:

```
screenshots/
├── home-page.png
├── health-endpoint.png
├── docker-container.png
├── ec2-instance.png
├── github-actions.png
```

---

# 📚 Learning Objectives

This project demonstrates practical experience with:

- Building Python web applications
- Flask application structure
- REST API development
- Git and GitHub workflows
- Docker image creation
- Docker container management
- Linux server administration
- AWS EC2 deployment
- SSH authentication
- Production deployment using Gunicorn
- Continuous Integration
- Continuous Deployment
- Infrastructure as Code
- Configuration Management

---

# 🔮 Future Improvements

The project roadmap includes:

- GitHub Actions CI Pipeline
- Automatic Deployment to AWS EC2
- Docker Compose
- Nginx Reverse Proxy
- HTTPS using Let's Encrypt SSL
- Terraform Infrastructure
- Ansible Configuration
- CloudWatch Monitoring
- Prometheus Metrics
- Grafana Dashboard
- Multi-Environment Deployment
- Load Balancer
- Auto Scaling
- RDS Database Integration

---

# 📖 Useful Commands

## Git

```bash
git status

git add .

git commit -m "Commit message"

git push origin main
```

## Docker

```bash
docker build -t flask-app .

docker images

docker ps

docker logs flask-container

docker stop flask-container

docker start flask-container

docker restart flask-container
```

## Linux

```bash
sudo systemctl status docker

docker --version

pwd

ls

cd

git pull
```

---

# 📈 Resume Highlights

This project demonstrates experience with:

- Python Development
- Flask
- Docker
- Linux
- Git
- GitHub
- AWS EC2
- Ubuntu Administration
- SSH
- Gunicorn
- CI/CD
- Infrastructure Automation
- Cloud Computing
- DevOps Best Practices

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# 🛡️ Best Practices Followed

- Clean project structure
- Virtual environment for dependency isolation
- Git version control
- Docker containerization
- Production-ready Gunicorn server
- Health check endpoint
- Unit testing with Pytest
- Modular Flask application
- AWS cloud deployment
- Linux administration
- Documentation using Markdown

---

# 📋 Project Milestones

| Milestone | Status |
|-----------|--------|
| AWS Account Setup | ✅ Completed |
| IAM User Creation | ✅ Completed |
| Git Installation | ✅ Completed |
| GitHub Repository | ✅ Completed |
| Python Environment | ✅ Completed |
| Flask Application | ✅ Completed |
| HTML Frontend | ✅ Completed |
| Unit Testing | ✅ Completed |
| Docker Containerization | ✅ Completed |
| AWS EC2 Deployment | ✅ Completed |
| Gunicorn Setup | ✅ Completed |
| Docker Restart Policy | ✅ Completed |
| GitHub Actions CI | 🚧 In Progress |
| Automatic Deployment | ⏳ Planned |
| Terraform | ⏳ Planned |
| Ansible | ⏳ Planned |
| Monitoring | ⏳ Planned |

---

# 📂 Repository

GitHub Repository:

https://github.com/sreepradat/aws-devops-cicd-project

---

# 👩‍💻 Author

**Sreeprada T**

Aspiring DevOps & Cloud Engineer

### Skills

- Python
- Flask
- Docker
- Linux
- Git
- GitHub
- AWS EC2
- Ubuntu
- DevOps
- CI/CD
- Cloud Computing

GitHub Profile:

https://github.com/sreepradat

---

# 📄 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project for educational and personal learning purposes.

---

# 🎯 Project Status

## Current Status

✅ Successfully deployed on an AWS EC2 Ubuntu instance using Docker.

### Completed

- Flask application development
- Docker containerization
- AWS EC2 deployment
- Gunicorn production server
- Health endpoint
- Unit testing
- GitHub repository
- Linux server setup

### Next Steps

- GitHub Actions Continuous Integration
- Automated Deployment to AWS EC2
- Terraform Infrastructure as Code
- Ansible Configuration Management
- Nginx Reverse Proxy
- Monitoring with CloudWatch
- Prometheus & Grafana Dashboard

---

## ⭐ Acknowledgements

This repository was created as a hands-on DevOps portfolio project to demonstrate practical cloud and automation skills using AWS and modern DevOps tools.

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

**Thank you for visiting this project!**
