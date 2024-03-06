# Note Taking App

The Note Taking App is a Django-based web application for creating, retrieving, updating notes. It provides a simple and efficient way to manage your notes.

## Features

- **Create Notes**: Add new notes with a title and body content.
- **Retrieve Notes**: View individual notes by their unique identifier.
- **Update Notes**: Modify the title or body content of existing notes.
- **Filtering**: Filter notes based on their title using a case-insensitive substring match.

## Installation

1. Clone the repository:
      gh repo clone Ashish-jukaria/Note-App

2. Navigate to project directory
      cd note_taking_app

3.   Create the Virtual environment

      pip install virtualenv
      virtualenv env

4.    Start the Virtual env
          source env/bin/activate

5.    Install Dependencies

        pip install -r requirements.txt

6.    Apply Migrations

        python manage.py makemigrations
        python manage.py migrate
7.    Run the App
          python manage.py runserver


Configuration
No additional configuration is required for basic usage.
Customize Django settings (e.g., database configuration, secret key) as needed in settings.py.


API Endpoints
Create Note: POST /notes/create/
Retrieve/Update/Delete Note: GET/PUT/ /notes/<int:pk>/
List Notes: GET /notes/

Built With
Django - Web framework for building web applications in Python
Django REST Framework - Toolkit for building Web APIs


       

      

