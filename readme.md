# Exchange Rate App with Docker Compose

This is a Docker Compose configuration for an Exchange Rate App. It includes services for the backend, frontend, and a MySQL database. Use this setup to quickly run the app in a containerized environment.

## Prerequisites

Before you begin, ensure that you have the following tools installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-repo/exchange-rate-app.git
   cd exchange-rate-app
   ```

2. Rename example.env -> .env inside the backend and frontend directory and configure your backend environment variables as needed.

3. Run the following Docker Compose command to start the application:
    ```bash
    docker-compose up -d build
    ```
4. Access the frontend application in your browser at **http://localhost:8080**.

### Services
1. Backend
        Build Path: ./backend
        Port: 8000
        Description: The backend service for your Exchange Rate App.
2. Frontend
        Build Path: ./frontend
        Port: 8080
        Description: The frontend web application for the Exchange Rate App.
3. Database
    Image: MySQL (Latest)
    Container Name: mysql-container
    Port: 3306
    Description: The MySQL database used by the Exchange Rate App.
    Healthcheck: The database health is checked using a curl command.

### TODO
1. Monitoring
Consider implementing monitoring using tools like Prometheus and Grafana. Create separate services for these tools and configure them to collect and visualize metrics from your application services.

2. CI/CD
For Continuous Integration and Continuous Deployment (CI/CD), you can use Jenkins, Travis CI, GitLab CI/CD, or GitHub Actions. Set up a CI/CD pipeline to automate building, testing, and deploying your Exchange Rate App when changes are pushed to your version control repository.

3. Cache
Some implementation to avoid frequent db/network calls. Tool like redis.

4. Performance Considerations
Some decision were made just to get it working, depends on real use case db schema could be different.