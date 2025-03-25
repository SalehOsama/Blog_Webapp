# Blog Web Application using Django

# About Project:
A Django-based blog web application that allows users to create, read, update, and delete blog posts. The application also includes user profile management and essential authentication features such as user registration, login, and logout.

## Features:
* Register, log in, and log out securely.
* Create, Read, update, and delete blog posts.
* Manage user profiles for a personalized experience.
  
# Installation:
## On Local Machine

The Project is based on Python version: **Python 3.12.6**. Make sure that in your system **python** is installed and the python --version should be **Python 3.12.6** or **above**.

Open Command Prompt and create a virtualenv within your VM instance, activate it, and install all the mentioned dependencies (With the help of pip).
* Dependencies :
    ```
    $ pip install django-crispy-forms
    ```
    ```
    $ pip install crispy-bootstrap4
    ```
    ```
    $ pip install Pillow
    ```

  Your Project_Task directory looks like:
  
    * Django_Project (Project cloned or downloaded)
    * venv
    * .idea
  

Now, let's run the project. Open Command Prompt and set the path to the project.

For Example, My Project is located on the desktop.

```Command Prompt
    E:\Osama\Django\django_Project\Django_Project>
```
Run the command below to run a project at localhost.
```Command Prompt
E:\Osama\Django\django_Project\Django_Project>python manage.py runserver
```

The **URL** which you will get when you run it in your Web browser:**http://127.0.0.1:8000**. Copy the URL and open it in your web browser to access the running project.
