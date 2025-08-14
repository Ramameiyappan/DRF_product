🌟 Project Overview

This project is a simple eCommerce API designed to practice Django REST Framework and session-based authentication. It allows users to register, login, search products, add to cart, view cart history, and delete items. Only a superuser can add products.

This is not a production-ready application, but a learning project to implement REST APIs with Django.

🏗️ Project Structure

The project is divided into three main apps:

users – Handles user registration and login.

products – Allows users to search for products by name.

addcart – Manages adding products to the cart, viewing cart history, and deleting products from the cart.

Database tables:

user – Stores user credentials and information.

product – Stores product information (name, price, description, etc.).

cart – Stores products added to each user’s cart.

⚡ Features
User Features

Register as a new user.

Login to access products and cart.

Search for products by name.

Add products to the cart.

View cart history.

Delete items from the cart.

Admin Features

Only superuser can add new products.

🛠️ Tech Stack

Backend: Django, Django REST Framework

Database: MySQL

Authentication: Session Authentication

APIs: RESTful endpoints for all operations
