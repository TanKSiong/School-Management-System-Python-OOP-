# EduCore Management System

Welcome to the **EduCore Management System**! This application has been newly refactored into a layered architecture running on a modern Flask-based RESTful API with SQLite database integration.

## 🏗️ Architecture Overview

The system has been restructured dynamically to improve modularity, scalability, and code reusability:
- **`app.py`**: The main entry point for the Flask server.
- **`models/`**: Handles database connection and structure, including the initial migration script (`database.py`) transferring data seamlessly from legacy CSV files into SQLite.
- **`routes/`**: Flask Blueprints dictating structured RESTful API access (`student_routes.py`, `employee_routes.py`, and `academic_routes.py`).
- **`services/`**: The core business logic handlers keeping endpoints lightweight and reusable. Complex calculations (attendance, metrics, stats) live here.
- **`utils/`**: Application-wide helpers such as customized Exception handling (`exceptions.py`) returned in cleanly formatted JSON payloads.
- **`web_ui/`**: The frontend portal powered by elegant HTML/JS that interacts purely functionally with backend JSON APIs.

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

## ✨ Features Implemented
- **RESTful Endpoints**: Legacy generic command actions (like `/api/action`) have been effectively transitioned into isolated, HTTP method compliant endpoints (`GET`, `POST`, `PUT`, `DELETE`).
- **Improved Maintainability**: Routing code and business computation (like attendance evaluation and grade tallying) are strictly separated.
- **Strengthened Frontend**: The front-facing interface communicates predictably through JSON logic, ready for frontend evolution if desired. 
- **Error Handling**: A customized standard for catching issues (`APIError`, `NotFoundError`, etc.) that relays helpful and structured debug info back to the web portal!
