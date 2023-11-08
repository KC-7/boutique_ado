# Boutique Ado

[Boutique Ado](https://kc-boutique-ado-fb080e3c3917.herokuapp.com/) is a full-featured e-commerce platform built with Django, designed for a superior online shopping experience. It allows for a seamless flow from product browsing to purchase and user profile management.

**Live Link: https://kc-boutique-ado-fb080e3c3917.herokuapp.com/**

## Technology Stack

- **Backend**: Django, Python
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Static & Media Storage**: Amazon S3
- **Authentication**: Django Allauth
- **Payment Processing**: Stripe
- **Email Service**: SMTP with Gmail or console-based (for development)

## Installation and Setup

To get a local copy up and running, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies with `pip install -r requirements.txt`.
3. Set environment variables for `SECRET_KEY`, database configuration, email service, and Stripe API keys.
4. Run `python manage.py migrate` to create the database schema.
5. Start the local server with `python manage.py runserver`.

## Project Structure

- `boutique_ado/`: The main project directory containing settings and root routing configurations.
- `bag/`: An app managing shopping bag functionality.
- `checkout/`: Handles payment processing, order records, and webhooks.
- `home/`: Manages the homepage and other static pages.
- `media/`: Media files like images uploaded by the admin.
- `products/`: Product management — addition, editing, and deletion.
- `profiles/`: User profile creation and management.
- `static/`: Contains static assets such as CSS, JavaScript, and images.
- `templates/`: Django HTML templates for rendering views.

## Features

- Product search and categorization.
- User authentication and session management.
- Shopping bag and checkout with order summary.
- Payment processing with Stripe integration.
- User profile management for order history and information storage.

## Running Tests

To run automated tests, use:

```sh
python manage.py test
```

Ensure you have testing configurations set up as per Django's best practices.

## Future Improvements

- UI/UX enhancements.
- Integration of advanced analytics.
- Expansion of product categories and inventory management features.

## Acknowledgments

Special thanks to the Code Institute for this walk through project. This project is a part of their Full Stack Developer Course to demonstrate the capabilities of Django in building complex web applications.
ChatGPT for generating the README.
