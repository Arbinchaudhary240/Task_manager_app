# Django Task Manager
A robust, timezone-aware Task Management application built with Django. This isn't just a simple "To-Do" list; it handles the complex parts of web development, like localized time offsets and custom template logic.

## 🚀 Features
- **User Authentication:** Secure registration, login, and logout.
- **Task CRUD:** Create, View, Update, and Delete tasks.
- **Search Functionality:** Real-time task filtering.
- **Security:** Logic-level isolation (Users can only see their own tasks).
- **Class-Based Views:** Built using Django's generic views for scalability.
- **Smart timezone Awarness:** 
Tasks are stored in UTC but automatically converted to the user's local time.
- **Human friendly Date filters:**
Instead of showing boring dates like 2026-01-28, the app uses a custom template tag (smart_date) to display:
-Today
-Tomorrow
-Yesterday
- **Integrated Overdue Logic:**
The system automatically identifies tasks that have passed their due date and marks them with a visual "Overdue" badge.
- **Robust Testing Suite:**
Includes automated Unit Tests to ensure:
-Tasks are saved with the correct time.
-The "Update" form pre-fills data accurately.
-The smart_date filter renders correctly in the browser.

🛠️ Technical Stack
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