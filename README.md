## Task Manager App
A clean, robust, and intuitive web application built with Python and Django to streamline daily task workflows. This application allows users to create, categorize, track, and manage their tasks efficiently with secure user authentication and an interactive dashboard.

## Key Features
User Authentication & Security: Secure user signup, login, and logout functionalities to ensure data privacy.

Task CRUD Operations: Complete control to Create, Read, Update, and Delete tasks.

Task Categorization: Group tasks by status (e.g., Pending, In Progress, Completed) and set priorities (High, Medium, Low).

Responsive Dashboard: A clean user interface optimized for both desktop and mobile views.

Due Date Tracking: Stay on top of deadlines with visual reminders for upcoming and overdue items.

## Tech Stack
Backend Framework: Python  & Django ⚙️

Database: SQLite (Default / Development)

Frontend: HTML5, CSS3, Bootstrap (or Tailwind)

## Getting Started & Installation
Follow these steps to set up the project locally on your machine.

Prerequisites
Make sure you have Python installed (v3.10 or higher recommended). You can verify by running:

Bash
python --version
Setup Steps

1. Clone the Repository

Bash
git clone https://github.com/Arbinchaudhary240/Task_manager_app.git
cd Task_manager_app

2. Create and Activate a Virtual Environment

On Windows:  

Bash
python -m venv venv
venv\Scripts\activate

On macOS/Linux:  

Bash
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies  

Bash
pip install -r requirements.txt

4. Run Database Migrations  

Bash
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (Optional - for Admin Panel Access)

Bash
python manage.py createsuperuser

6. Start the Development Server

Bash
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/ to explore the app!

📂 Project Structure

Task_manager_app/
│
├── core/                  # Main project configuration folder (settings, urls, etc.)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/                 # Primary application logic app
│   ├── migrations/
│   ├── templates/         # HTML files for UI rendering
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py          # Database schemas (User, Task structures)
│   ├── urls.py            # Route mappings for tasks
│   └── views.py           # Request-response controllers
│
├── manage.py              # Django administrative command script
├── requirements.txt       # Dependencies list
└── README.md              # Project documentation

🔒 Security & Best Practices

Environment Variables: Never commit the SECRET_KEY or sensitive database credentials directly to GitHub. Use a .env file with django-environ or python-dotenv.

Database Seeding: Ensure DEBUG = True is only used during development and turned off (False) in production environments.