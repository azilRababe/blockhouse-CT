Data visualization dashboard that includes various types of charts for displaying data. It uses Chart.js for Bar, Line, and Pie charts, and ApexCharts for Candlestick charts.

## Libraries and Tools Used

    Frontend:
        Next.js: React framework for server-side rendering and static site generation.
        Chart.js: For Bar, Line, and Pie charts.
        ApexCharts: For Candlestick charts.
        Tailwind CSS: For styling the application.
        Axios: For making HTTP requests.

    Backend:
        Django: Python framework for building web applications.
        Django REST Framework: For creating RESTful APIs.

    Docker: For containerizing the application.

Setup and Running the Application
Prerequisites

    Docker installed on your machine.
    Docker Compose installed on your machine.

Steps to Set Up and Run

    Clone the Repository

    If you have the project directory available, skip this step. If you don't, you need to obtain it. This could be done via a zip file or another version control system if GitHub is not an option.

    Build and Run the Docker Containers

    Open a terminal and navigate to the root of the project directory. Run the following command to build and start the Docker containers:

    ```docker-compose up --build
    ```

This command builds the Docker images and starts the containers as defined in your docker-compose.yml file.

Access the Application

    Frontend: Open your web browser and navigate to http://localhost:3000 to view the Next.js frontend.
    Backend: The Django backend should be accessible at http://localhost:8000.

Stopping the Containers

To stop the Docker containers, run:

```docker-compose down

```
# blockhouse-CT
