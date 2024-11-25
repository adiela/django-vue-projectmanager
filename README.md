# Django Vue Project Management Tool

## Instructions on how to run the Backend and Frontend

### Running the Backend

1. Navigate to the backend directory:
    ```sh
    cd backend
    ```

2. Create virtual environment:
    ```
    python3 -m venv .venv
    ```

3. Activate virtual environment:
    ```
    source .venv/bin/activate
    ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Create .env file and add environment variables reference .env.example
    ```
    touch .env
    ```

6. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

7. Start the backend server:
    ```sh
    python manage.py runserver
    ```

### Running the Frontend

1. Navigate to the frontend directory:
    ```sh
    cd frontend
    ```

2. Install the required dependencies:
    ```sh
    npm install
    ```

3. Start the frontend server:
    ```sh
    npm run dev
    ```

### Accessing the Application

- The backend server will be running on `http://localhost:8000` (or the port specified in your configuration).
- The frontend server will be running on `http://localhost:3000` (or the port specified in your configuration).

Open your web browser and navigate to the frontend URL to access the application.