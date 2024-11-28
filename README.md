# Authentication-API-with-JWT-in-Django-REST-Framework
This project is the backend of the login system. The code of the project is in Django format.Along with Django, REST Framework is also used to set up API and JSON Web Tokens(JWT) helps to create a Token Authentication.

This project consists of processes like registration, login, get user details, change password and send reset password email. Access and Refresh Tokens are generated while registration and login.The accsss token of registration is used to retrieve user detail and change password. When email is sent to reset password then it verifies the email and sends the reset link to the email which is seen on terminal.

## Installation

1. Clone the Project

```bash
  https://github.com/kanakamamidiakhil/Authentication-API-with-JWT-in-Django-REST-Framework.git
  cd Authentication-API-with-JWT-in-Django-REST-Framework
```
2. Create Virtual Environment in Windows

```bash
 python -m venv env
 env\Scripts\activate
 ```

3. Install the required packages:

```bash
 pip install -r requirements.txt
 ```

4. Apply migrations:

```bash
 python manage.py migrate
 ```

5. Run the Project

```bash
 python manage.py runserver
 ```
