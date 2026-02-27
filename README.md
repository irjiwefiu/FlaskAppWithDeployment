# FlaskAppWithDeployment

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/irjiwefiu/FlaskAppWithDeployment.git)

This repository contains a simple Flask web application designed for deployment. It serves as a single-page invitation for a music event, complete with a contact form. The project is fully containerized using Docker and includes a CI/CD pipeline with GitHub Actions to automate deployment to an AWS EC2 instance via Amazon ECR.

## Features

- **Flask Backend**: A lightweight web server built with Flask (`app.py`) handles routing and form submission.
- **Single-Page Frontend**: The user interface is a responsive single-page HTML template (`templates/index.html`) styled with custom CSS.
- **Custom Logging**: A dedicated logging module (`log.py`) creates timestamped log files in a `logs/` directory and simultaneously outputs logs to the console.
- **Docker Containerization**: A `Dockerfile` is provided to build a production-ready image using Gunicorn as the WSGI server.
- **Automated CI/CD**: A GitHub Actions workflow (`.github/workflows/aws.yml`) automates the process of building the Docker image, pushing it to Amazon ECR, and deploying it on a self-hosted runner (e.g., an EC2 instance).

## Project Structure

```
.
├── .github/workflows/aws.yml   # GitHub Actions workflow for CI/CD
├── static/                     # Static files (CSS, images)
├── templates/index.html        # Main HTML template
├── app.py                      # Core Flask application logic
├── log.py                      # Custom logger configuration
├── Dockerfile                  # Defines the Docker image
├── requirements.txt            # Python dependencies
└── LICENSE
```

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Local Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/irjiwefiu/FlaskAppWithDeployment.git
    cd FlaskAppWithDeployment
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Running with Docker

You can also build and run the application as a Docker container.

1.  **Build the Docker image:**

    ```bash
    docker build -t flask-app-deployment .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -d -p 5000:5000 --name my-app-container flask-app-deployment
    ```
    The application will be running inside the container and accessible at `http://localhost:5000`.

## CI/CD Deployment Pipeline

This repository is configured with a GitHub Actions workflow to automatically deploy the application to a self-hosted runner, such as an AWS EC2 instance.

### How It Works

The workflow is defined in `.github/workflows/aws.yml` and consists of two main jobs:

1.  **`continuous-integration`**:
    - Triggered on every push to the `main` branch.
    - Builds the Docker image from the `Dockerfile`.
    - Logs into Amazon Elastic Container Registry (ECR).
    - Tags the image with `latest` and pushes it to your ECR repository.

2.  **`continuous-deployment`**:
    - Depends on the successful completion of the `continuous-integration` job.
    - Runs on a `self-hosted` runner.
    - Pulls the newly pushed Docker image from ECR.
    - Stops and removes the currently running container (`my-app-container`).
    - Starts a new container with the updated image, exposing port 5000.

### Required GitHub Secrets

To enable the CI/CD pipeline, you must configure the following secrets in your GitHub repository settings:

- `AWS_ACCESS_KEY_ID`: Your AWS IAM user access key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS IAM user secret access key.
- `AWS_DEFAULT_REGION`: The AWS region where your ECR repository is located (e.g., `us-east-1`).
- `ECR_REPOSITORY`: The name of your ECR repository.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.
