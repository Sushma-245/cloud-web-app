# Cloud-Based Web Application Architecture with Automated CI/CD

A high-performance, cloud-native REST API built with Python and FastAPI, deployed on an AWS EC2 instance, and fully automated using a GitHub Actions CI/CD pipeline.

## 🚀 Live Demo & Documentation
* **Live API Endpoints:** [http://13.126.206.96](http://13.126.206.96)
* **Interactive API Documentation:** [http://13.126.206.96/docs](http://13.126.206.96/docs)

## 🏗️ System Architecture
* **Backend Framework:** FastAPI (Python 3) driven by a production-grade Uvicorn ASGI server.
* **Cloud Infrastructure:** Amazon Web Services (AWS) EC2 Virtual Instance running Amazon Linux 2023.
* **Automation (CI/CD):** GitHub Actions Workflow utilizing encrypted Repository Secrets for automated, secure, zero-downtime SSH deployments on every code push to the `main` branch.

## 📁 Repository Structure
* `app.py` - Core REST API application logic and endpoints.
* `requirements.txt` - Python package dependencies (`fastapi`, `uvicorn`, `pydantic`).
* `.github/workflows/deploy.yml` - Complete GitHub Actions automation workflow engine.
* `.gitignore` - System security exclusions configuration.
