->DevOps End-to-End CI/CD Pipeline Project

Flask App • Docker • DockerHub • GitHub Actions • Kubernetes • Minikube

This project demonstrates a complete DevOps workflow—from source code to containerization, automated testing, CI/CD pipeline, and Kubernetes deployment.

Project Highlights

->Flask web application

-> Unit testing with pytest

-> Containerization using Docker

-> Automated CI/CD pipeline using GitHub Actions

-> DockerHub image publishing

-> Kubernetes Deployment + Service

-> Minikube for local cluster orchestration

* Future-ready design for cloud deployment (DigitalOcean / Civo)

->Tech Stack

Language-	               Python (Flask),
Container-               Docker,
CI/CD-	                 GitHub Actions,
Registry-	               DockerHub,
Orchestration-	         Kubernetes,
Local Cluster-	         Minikube,
Testing-	               Pytest.

->Architecture Overview

Developer → GitHub → GitHub Actions CI/CD → DockerHub → Kubernetes (Minikube)

* CI Pipeline

Runs on every push to (main)

Steps:

 -Checkout Code

 -Setup Python

 -Install Dependencies

 -Run Tests

 -Docker Build
 
 -Docker Push (latest + version tag)

 * CD Pipeline (Local Minikube)

Local script: (deploy_local.sh)

Applies Kubernetes manifests:

   -deployment.yaml

   -service.yaml

Pulls latest image from DockerHub

Exposes service on Minikube URL

-> Folder Structure
devops-end-to-end/
│── app.py

│── tests/

│── Dockerfile

│── requirements.txt

│── k8s/

│    ├── deployment.yaml

│    └── service.yaml

│── deploy_local.sh

│── .github/

│     └── workflows/

│          └── ci-cd.yml

* Docker Setup

-> Build image locally: 

docker build -t devops-end-to-end:local .

-> Run container:

docker run -p 8000:8000 devops-end-to-end:local

* Kubernetes Deployment (Minikube)

  -Start Minikube:

  minikube start --driver=docker

  -Apply manifests:

  kubectl apply -f k8s/

  -Get service URL:

  minikube service devops-app-service --url

* GitHub Actions CI/CD Workflow

  -Located at:

  .github/workflows/ci-cd.yml

  -Pipeline includes:

  *Install dependencies

  *Run pytest

  *Build Docker image

  *Push to DockerHub

  *(Optional future) Deploy to cloud cluster

  * DockerHub Repository

  -Your DockerHub container image is automatically updated by GitHub Actions.

    **(https://hub.docker.com/r/<USER_NAME>/devops-end-to-end)**

  * API Response Example
 
    Deployed via Kubernetes:

    **{"message": "DevOps CI/CD Pipeline working!"}**

    * Future Enhancements

*Deploy to DigitalOcean or Civo Kubernetes

*Add Ingress + Cert-Manager for HTTPS

*Add Prometheus + Grafana monitoring stack

*Add Helm charts for packaging

*Implement ArgoCD for GitOps-based CD

About This Project

*This project is built as a complete DevOps demonstration covering:

* CI

* CD

* Containerization

* Cluster deployment

* Automated workflows


*Author

**Devined4spd**
Feel free to connect or collaborate!
  

  






