# Todo list

The Todo App is a comprehensive task management API designed to help users manage their tasks and groups effectively. Developed using Python and Django Rest Framework (DRF), this application is containerized with Docker and uses PostgreSQL as its database. It is built to be scalable and efficient, featuring Nginx as a reverse proxy and utilizing GitHub Actions for continuous integration and deployment.

## 🚀 Features

- **User Authentication:** Secure user registration and token-based authentication.
- **Task Management:** Create, update, delete, and view tasks with various statuses and priorities.
- **Group Management:** Organize tasks into groups for better categorization and management.
- **API Documentation:** Interactive Swagger documentation for easy API navigation.

## 🛠️ Tech Stack

- **Backend:** Python, Django Rest Framework (DRF)
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Web Server:** Nginx
- **CI/CD:** GitHub Actions

## 🌐 URL Endpoints
#### Authentication & User Management
- **User Registration:** `/api/user/create/`
- **User Login (Token Creation):** `/api/user/token/`
- **User Profile:** `/api/user/me/`
#### Tasks
- **List & Create Tasks:** `/api/todo/tasks/`
- **Retrieve, Update & Delete Task:** `/api/todo/tasks/<uuid:id>/`
- **Clap Article:** `/api/v1/articles/<uuid:article_id>/clap/`
#### Groups
- **List & Create Groups:** `/api/todo/groups/`
- **Retrieve, Update & Delete Group:** `/api/todo/groups/<uuid:id>/`
#### API Documentation
- **Swagger Documentation:** `/api/docs/`
- **API Schema:** `/api/schema/`

## 📦 Installation 
Clone the repository:
```bash
git clone https://github.com/YaroslavMarkivskyi/todo-app.git
```
Navigate to the project directory:
```bash
cd todo-app
```
Set up and run the application using Docker Compose:
```bash
docker-compose up --build
```
Access the application at:
- API Documentation - [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- Admin Panel - [http://localhost:8000/admin/](http://localhost:8000/admin/)
##### To create a superuser after setting up the application with Docker, follow these steps:
Run the following command to enter the Docker container for your Django application:
```bash
docker-compose run --rm app sh
```
Inside the container, create a superuser using Django's createsuperuser command:
```bash
python manage.py createsuperuser
```
Follow the prompts to enter your desired superuser credentials (username, email, and password).

Once complete, exit the container by typing:
```bash
exit
```
