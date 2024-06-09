# Attendance Management System

## Steps to Set Up and Run the Application

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2. Setup the environment variables:

    Create a `.env` file with the following contents:
    ```bash
    POSTGRES_DB=attendance_db
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    ```

3. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

4. Apply migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
6. Access the application at `http://localhost:8000`.

## Assumptions

* The application is designed to run in a local development environment.
* The system assumes a single laptop with a webcam for attendance marking.

## Additional Features

* **Face Recognition:** Add real-time face recognition for attendance verification.
* **Notification:** Implement email notifications for managers and staff.
* **Reporting:** Generate attendance reports for managers.
