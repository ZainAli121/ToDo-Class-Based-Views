# ToDo-Class-Based-Views
This is a simple todo app built using Django and Django REST Framework (DRF), with class-based views (CBVs) for the frontend and APIs for authentication using JWT and task CRUD operations.

# Preview
![Screenshot (458)](https://github.com/ZainAli121/ToDo-Class-Based-Views/assets/129948136/4efd152f-6a69-4509-b323-8627e5ac15bc)


# Installation
1. Clone the repository
    ```markdown

    $ git clone https://github.com/ZainAli121/ToDo-Class-Based-Views.git


2. Create the virtual env
    ```markdown

    python -m venv venv

3. Activate the virtual env
    ```markdown

    venv\Scripts\activate

4. Install the dependencies
    ```markdown

    python -m pip install -r requirements.txt

5. Move to the project directory
    ```markdown

    cd core

6. Run the migrations
    ```markdown

    python manage.py migrate

7. Run the server
    ```markdown

    python manage.py runserver


# Usage
1. Open the browser and go to http://127.0.0.1:8000/

# APIs
+ Authentication API (JWT):
    + POST /api/token/: Obtain JWT token by providing username and password.
    + POST /api/token/refresh/: Refresh JWT token by providing a valid refresh token.

+ Task API:
    + GET /api/tasks/: Retrieve all tasks.
    + POST /api/tasks/: Create a new task.
    + GET /api/tasks/{id}/: Retrieve a specific task by ID.
    + PUT /api/tasks/{id}/: Update a task by ID.
    + DELETE /api/tasks/{id}/: Delete a task by ID.


# Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.