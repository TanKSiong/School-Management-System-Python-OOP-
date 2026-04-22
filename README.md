# 🌐 School Management System (Web-Based with Python & HTML)

## 📌 Overview

This project is a web-based School Management System that integrates a Python backend logic with a HTML-based web interface.

The system allows users to manage student records, academic data, and administrative operations through a user-friendly interface, replacing the original command-line version with a more practical and interactive solution.
<img width="1812" height="820" alt="image" src="https://github.com/user-attachments/assets/e196730e-6f62-40da-96c6-73602faeca54" />

<img width="1523" height="823" alt="image" src="https://github.com/user-attachments/assets/888badfd-05eb-4b10-b888-bec2b134e8bc" />

---

## 🚀 Features

* Student information management
* Admin panel for system control
* Web-based user interface (UI)
* Data handling using CSV files
* Integration between Python logic and HTML&CSS frontend
* Modular system design

---

## 🛠 Tech Stack

* Backend Logic: Python (OOP)
* Web Layer: HTML
* Frontend: HTML, CSS, JavaScript
* Data Storage: CSV files

---


## 🏗️ Architecture Overview

The system has been restructured dynamically to improve modularity, scalability, and code reusability:
- **`app.py`**: The main entry point for the Flask server.
- **`models/`**: Handles database connection and structure, including the initial migration script (`database.py`) transferring data seamlessly from legacy CSV files into SQLite.
- **`routes/`**: Flask Blueprints dictating structured RESTful API access (`student_routes.py`, `employee_routes.py`, and `academic_routes.py`).
- **`services/`**: The core business logic handlers keeping endpoints lightweight and reusable. Complex calculations (attendance, metrics, stats) live here.
- **`utils/`**: Application-wide helpers such as customized Exception handling (`exceptions.py`) returned in cleanly formatted JSON payloads.
- **`web_ui/`**: The frontend portal powered by elegant HTML/JS that interacts purely functionally with backend JSON APIs.
--- 

## 🚀 How to Run

1. Make sure you have python installed along with the required backend libraries:
   ```bash
   pip install flask pandas numpy
   ```
2. Start the Flask server:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

*Note: The first time you launch `app.py`, the system will automatically parse the existing `.csv` files and migrate all your data into a highly efficient SQLite file (`educore.db`).*


## 📊 System Workflow

1. User interacts with the web interface (PHP)
2. Requests are processed and passed to backend logic
3. Python modules handle data processing
4. Data is stored/retrieved from CSV files
5. Results are displayed on the UI

---

## 🧩 System Design Highlights

* Hybrid architecture (Python + PHP)
* Transition from CLI to web-based system
* Separation of frontend and backend logic
* Lightweight data management using CSV

---

## ⚠️ Limitations

* No database integration (CSV-based storage)
* Limited scalability for large systems
* Basic UI design
* Integration between PHP and Python is not fully optimized

---

## 💡 Future Improvements

* Replace CSV with MySQL database
* Develop REST API for better integration
* Improve UI/UX design
* Add authentication and role-based access control

---

## 🎯 Motivation

This project was enhanced from a command-line system into a web-based application to improve usability and demonstrate full-stack development capabilities, combining backend logic with a functional user interface.

---

## 👤 Author

* Tan Kheng Siong
