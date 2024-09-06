# Description

This is a data visualization dashboard that includes various types of charts for displaying data. It uses Chart.js for Bar, Line, and Pie charts, and ApexCharts for Candlestick charts. The application consists of a Next.js frontend and a Django backend, with Django REST Framework (DRF) providing API services for the frontend.

## Libraries and Tools Used

Frontend:

- Next.js: React framework for server-side rendering and static site generation.
- Chart.js: For rendering Bar, Line, and Pie charts.
- ApexCharts: For rendering Candlestick charts.
- Tailwind CSS: Utility-first CSS framework for styling.
- Axios: To handle HTTP requests to the backend API.

Backend:

- Django: Python framework for building web applications.
- Django REST Framework (DRF): Used for creating RESTful APIs.

## Setup and Running the Application

### Prerequisites

- Node.js and npm for the frontend.
- Python and pip for the backend.
- Virtual environment for Python (optional but recommended).

### Steps to Set Up and Run

> Backend (Django)

1. Navigate to the backend directory:

```
 cd backend
```

2. Create and activate a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

4. Run the Django development server:

```
python manage.py runserver
```

<b>The backend will be accessible at http://localhost:8000.</b>

> Frontend (Next.js)

1. Navigate to the frontend directory:

```
cd frontend
```

2. Install the required Node.js packages:

```
npm install
```

3. Create a .env file in the frontend directory and add your environment variables (e.g., API base URL):

```
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

4. Run the Next.js development server:

```
npm run dev
```

<b>The frontend will be accessible at http://localhost:3000.</b>

## Thought Process and Approach

- **Frontend-Backend Separation**: The frontend and backend are built independently, communicating via APIs. This structure allows for flexibility, as both parts can be scaled and updated separately. -** Data Visualization**: The decision to use Chart.js for Bar, Line, and Pie charts was due to its ease of use and wide community support. ApexCharts was selected for Candlestick charts, as it offers better options for financial visualizations.
- **Next.js**: The project uses Next.js for server-side rendering, improving SEO and load times.
- **TypeScript Integration**: Adding TypeScript to the Next.js application will enhance type safety and development efficiency, complementing the Django backend setup.
- **State Management**: Integrating state management solutions such as Redux or Context API can streamline state handling across components. (in progress)
- **Docker**: Facilitates the streamlined setup and management of both the Next.js frontend and the Django backend. (in progress)
