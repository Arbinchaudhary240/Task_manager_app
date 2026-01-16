# Django Task Manager
A professional, multi-user Task Management system built as a foundation for my **Google Summer of Code** journey. This project demonstrates core web development principles: CRUD logic, User Authentication, and Responsive Design.

## 🌟 Key Features

* **User Accounts:** Secure Login/Signup system using Django's built-in Auth.
* **Private Dashboards:** Each user has their own personal task list (User-Task ownership).
* **Full CRUD:** Create, Read, Update, and Delete functionality for task management.
* **Real-time Search:** Filter tasks instantly using the integrated search bar.
* **Responsive UI:** Styled with **Bootstrap 5** for seamless use on mobile and desktop.

## 🛠️ Tech Stack

* **Backend:** [Django 5.x](https://www.djangoproject.com/) (Python)
* **Frontend:** HTML5, Bootstrap 5
* **Database:** SQLite3 (Local development)
* **Version Control:** Git & GitHub

## ⚙️ Installation & Setup

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Arbinchaudhary240/gsoc-task-manager.git](https://github.com/Arbinchaudhary240/gsoc-task-manager.git)
   cd gsoc-task-manager

2. **Create a Virtual Environment:**
   ```bash
   python -m venv .venv
   # Actvate on windows:
   .\.venv\Scripts\activate

3. **Install Dependencies:**
   ```bash
   pip install -r requirement.txt

4. **Initialize Database:**
    ```bash
    python manage.py migrate

5. **Start the Development server:**
    python manage.py runserver

6. open http://127.0.0.1:8000/ in your browser.

# 📂 Project Structure:
- core/: Project configuration and settings.
- my_app/: Main application logic (Models,     Views, Templates).
- templates/: HTML files with Bootstrap integration.
- requirements.txt: List of all Python dependencies.