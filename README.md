# 🎓 School Management System

A simple CRUD-based web application for managing students, built with Django using the MVT (Model-View-Template) architectural pattern.

## 🚀 Features

- ➕ Add new students
- ✏️ Edit student information
- ❌ Delete students
- 📋 View all students
- 🔍 Simple and clean interface
- ⚡ Built with Django and SQLite

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite
- Bootstrap

## 🧩 Architecture

This project follows the **MVT (Model-View-Template)** pattern used in Django:

- **Model** — handles database structure and logic
- **View** — processes requests and responses
- **Template** — renders the frontend UI

## 📂 Project Structure

```bash
School_Management/
│── .idea/                         # IDE configuration files
│── Docker/                        # Docker configuration files
│
│── apps/                          # Django applications
│   ├── core/                      # Core application
│   ├── student_management/        # Student management CRUD app
│   └── __init__.py
│
│── media/
│   └── student_photos/            # Uploaded student photos
│
│── school_management/             # Main project configuration
│   ├── settings.py                # Project settings
│   ├── urls.py                    # Main URL configuration
│   ├── asgi.py                    # ASGI configuration
│   ├── wsgi.py                    # WSGI configuration
│   └── __init__.py
│
│── manage.py                      # Django management script
