# Authentication-API-with-JWT-in-Django-REST-Framework
This project is the backend of the login system. The code of the project is in Django format.Along with Django, REST Framework is also used to set up API and JSON Web Tokens(JWT) helps to create a Token Authentication.

This project consists of processes like registration, login, get user details, change password, send reset password email and reset email. Access and Refresh Tokens are generated while registration and login.The accsss token of registration is used to retrieve user detail and change password. When email is sent to reset password then it verifies the email and sends the reset link to the email which is seen on terminal. Once the uid and reset password token is entered in the url of reset password then reset of password is possible.

The operations of reset link is a prototype where the user details get stored in .env file and reset link is sent to that email after it is verified.
