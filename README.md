# Mini Shopping Cart Application

A fullstack Django shopping cart application with Docker integration.

## Features

- User registration and authentication
- Product browsing by categories
- Shopping cart functionality
- Responsive, user-friendly interface
- Docker containerization for web server and PostgreSQL database

## Technologies Used

- Django 4.2
- PostgreSQL
- Docker and Docker Compose
- Bootstrap 5 for frontend
- Crispy Forms for form rendering

## Setup Instructions

### Using Docker (Recommended)

1. Make sure you have Docker and Docker Compose installed on your system.
2. Clone this repository.
3. Navigate to the project directory.
4. Build and start the containers:

```bash
docker-compose up --build
```

5. Access the application at http://localhost:8000

### Load Dummy Data

To load sample products and categories into the database:

```bash
docker-compose exec web python manage.py load_dummy_data
```

### Admin Access

An admin user is automatically created when loading dummy data:
- Username: admin
- Password: admin123

Access the admin panel at http://localhost:8000/admin

## Project Structure

- `/cart` - Shopping cart functionality
- `/products` - Product models and views
- `/users` - User authentication and profiles
- `/templates` - HTML templates
- `/static` - Static files (CSS, JS, images)

## Usage

1. Browse products by category
2. Add items to your cart
3. Update quantities or remove items from your cart
4. Proceed to checkout (simulated)

## License

MIT