This project is a Django REST Framework based API that implements Role-Based Access Control (RBAC) with JWT Authentication.
Users are categorized into three roles:

Admin – Full access (Create, Read, Update, Delete)
Moderator – Can Read and Update
User – Can only Read

Features
Custom User model with roles (Admin, Moderator, User)
JWT Authentication (using djangorestframework-simplejwt)
Role-based permissions for APIs
User Registration, Login, Logout
Secure Refresh token Blacklisting
DRF ViewSets for easy CRUD operations

API Endpoints

Method	Endpoint	Description
POST	/api/accounts/register/	Register a new user
POST	/api/login/	Login to get Access and Refresh Token
POST	/api/token/refresh/	Refresh Access Token
POST	/api/accounts/logout/	Logout and blacklist Refresh Token
GET	/api/accounts/users/	List all users (depends on role)
POST/PUT/PATCH/DELETE	/api/accounts/users/<id>/	Modify user (depends on role)
