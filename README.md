# 🎓 Student ERP System

A full-stack **Student Enterprise Resource Planning (ERP) System** designed to streamline and manage student-related academic information through a centralized web application.

The project uses **FastAPI and Flask for the backend layer, PostgreSQL for database management, and a dedicated frontend** for user interaction.

---

## 🚀 Overview

The Student ERP System is built to provide a centralized platform for managing student and academic information.

Instead of maintaining student-related information across multiple systems or manually managing records, the application provides a structured web-based solution backed by a relational database.

### Key Goals

* Centralize student and academic information
* Provide a structured backend API
* Store and manage data using PostgreSQL
* Build a responsive and accessible frontend
* Follow a modular full-stack application architecture

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **FastAPI**
* **Flask**
* REST API architecture

### Database

* **PostgreSQL**

### Frontend

* HTML
* CSS
* JavaScript

### Development Tools

* Git & GitHub
* Visual Studio Code
* Postman / API testing tools

---


## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/xsparrkk/Student-ERP-System-FastAPI.git
```

```bash
cd Student-ERP-System-FastAPI
```

---

### 2. Set Up the Backend

Create and activate a virtual environment:

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

> If the `requirements.txt` file is located inside the backend directory, run the command from that directory.

---

## 🗄️ Database Configuration

This project uses **PostgreSQL** as its database.

Before running the application:

1. Install PostgreSQL.
2. Create a database for the project.
3. Configure the database connection according to the backend configuration.
4. Make sure the PostgreSQL server is running.

For security, avoid committing database passwords, API keys, or other credentials to GitHub.

---

## ▶️ Running the Application

Start the backend according to the FastAPI application entry point in the `backend` directory.

A typical FastAPI development command is:

```bash
uvicorn main:app --reload
```

The API documentation can then be accessed through:

```text
http://127.0.0.1:8000/docs
```

> The exact startup command may vary depending on the application entry point and project configuration.

---

## 🔌 API Documentation

FastAPI automatically provides interactive API documentation.

Once the backend is running:

**Swagger UI**

```text
http://127.0.0.1:8000/docs
```

**ReDoc**

```text
http://127.0.0.1:8000/redoc
```

These interfaces can be used to inspect and test the available API endpoints.

---

## 🔐 Environment Variables

For local development, sensitive configuration should be stored using environment variables rather than being hard-coded.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/student_erp
```

Do not commit `.env` files containing real credentials.

---

## 📌 Project Highlights

* Full-stack web application
* RESTful backend architecture
* FastAPI-based API development
* PostgreSQL relational database
* Separate frontend and backend structure
* Interactive API documentation through FastAPI
* Modular project organization
* Designed with scalability and maintainability in mind

---

## 🔮 Future Improvements

Some possible extensions for the project include:

* 🔐 Role-based authentication for students, faculty, and administrators
* 📊 Student performance and attendance dashboards
* 📅 Timetable and academic calendar management
* 📝 Assignment and examination management
* 📢 Announcements and notifications
* 📱 Mobile-friendly interface
* ☁️ Cloud deployment
* 🔄 Automated CI/CD pipeline
* 🔒 Improved authentication and authorization
* 📈 Analytics and reporting

---

## 🎯 Learning Outcomes

This project provides practical experience with:

* Full-stack application development
* REST API design
* FastAPI and Flask
* PostgreSQL database integration
* Frontend-backend communication
* Backend project structuring
* Git and GitHub workflow
* API testing and documentation

---

## 👩‍💻 Author

**Mimansha Pandit**

B.Tech Computer Science & Engineering

GitHub: [@xsparrkk](https://github.com/xsparrkk)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
