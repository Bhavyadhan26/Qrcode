# QR Menu System

A simple and efficient QR Menu system for restaurants or any other businesses. This system allows users to view the menu via a QR code, place orders, and the admin can manage orders and menu items.

## Features

- **User Side**: 
  - View menu items using a QR code.
  - Place orders with details such as name, and quantity.
  
- **Admin Side**:
  - View all placed orders.
  - Manage the menu items.
  
## Technologies Used

- **Backend**: Django
- **Database**: MySQL
- **Frontend**: HTML, CSS
- **Version Control**: Git, GitHub

## Setup

### Prerequisites

- Python (preferably 3.x)
- Git

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Bhavyadhan26/Qr_code.git
  
2. Navigate to the project directory:
```bash
  cd Qr_code
```
3. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate  # For Windows
```
4. Set up your database (replace these settings with your own credentials):
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',  # Example: localhost or a cloud service URL
        'PORT': '3306',
    }
}
```
5. Run the migrations to set up the database schema:
```bash
python manage.py migrate
```
6. Create a superuser to access the Django admin panel:
   ```bash
   python manage.py createsuperuser
```
7. Run the development Server
```bash
python manage.py runserver
```
8. Access the application in your browser at:
```bash
http://127.0.0.1:8000/
```



