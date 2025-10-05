# Airflow Task Orchestration 🚀

This repository demonstrates a simple yet effective use of Apache Airflow for orchestrating data tasks using DAGs (Directed Acyclic Graphs). It includes a working setup with Docker Compose and sample DAGs to illustrate task scheduling and logging.

## 📦 Project Structure

airflow-Task/ ├── dags/ # Contains DAG definitions and task logic
│ ├── add_images.py # DAG for image-related processing 
│ └── logs.py # DAG for logging tasks 
├── docker-compose.yaml # Docker setup for Airflow services 
└── logs/ # Output logs from DAG executions

Code

## ⚙️ Features

- **Dockerized Setup**: Easily spin up Airflow with Docker Compose.
- **Modular DAGs**: Each DAG is isolated for clarity and reusability.
- **Logging Pipeline**: Captures and stores logs from task executions.
- **Image Handling**: Includes a DAG for image processing tasks.

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/mohamedAbdelghafar1/airflow-Task.git
   cd airflow-Task
Start Airflow using Docker Compose:

bash
docker-compose up
Access the Airflow UI at http://localhost:8080

📌 Requirements
Docker & Docker Compose

Python (used within containers)

📈 Use Cases
This setup is ideal for:

Learning Airflow basics

Prototyping task orchestration pipelines

Demonstrating logging and image processing workflows

🖼️ Airflow UI Preview
<img width="949" height="485" alt="Screenshot 2025-10-04 092825" src="https://github.com/user-attachments/assets/6bdb25dc-f201-434e-abc2-605af769029b" />
<img width="958" height="482" alt="Screenshot 2025-10-04 093054" src="https://github.com/user-attachments/assets/0e469aae-a505-4ec2-baaf-79e793a1faf7" />
<img width="947" height="485" alt="Screenshot 2025-10-04 093859" src="https://github.com/user-attachments/assets/11141f91-9d3f-4cfc-99de-2328ee42aca9" />


