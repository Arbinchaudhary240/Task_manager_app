# Django Task Manager
A professional-grade Task Manager built with Django, focusing on Object-Oriented Programming (OOP) and secure Class-Based Views.

## 🚀 Features
- **User Authentication:** Secure registration, login, and logout.
- **Task CRUD:** Create, View, Update, and Delete tasks.
- **Search Functionality:** Real-time task filtering.
- **Security:** Logic-level isolation (Users can only see their own tasks).
- **Class-Based Views:** Built using Django's generic views for scalability.

## 🛠️ Technical Stack
- **Backend:** Django 6.0.1
- **Database:** SQLite (Development)
- **Architecture:** Class-Based Views (CBVs) with Mixins for security.
- **Testing:** Automated unit tests for core logic.
## ⚙️ Installation & Setup

## 🚦 Getting Started
1. Clone the repo: `git clone <your-repo-link>`
2. Create venv: `python -m venv .venv`
3. Install Django: `pip install django`
4. Run Migrations: `python manage.py migrate`
5. Start Server: `python manage.py runserver`
6. open http://127.0.0.1:8000/ in your browser.

## 🧪 Testing
Run the automated test suite:
```bash
python manage.py test

# 📂 Project Structure:
- core/: Project configuration and settings.
- my_app/: Main application logic (Models,     Views, Templates).
- templates/: HTML files with Bootstrap integration.
- requirements.txt: List of all Python dependencies.