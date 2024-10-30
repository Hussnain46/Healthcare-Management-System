<h1>Healthcare Management System</h1>
A comprehensive web-based Healthcare Management System built with Django, designed to streamline medical appointment booking, prescription management, and medical record tracking for patients and healthcare providers. This project includes secure user management, customizable appointment scheduling, and easy access to patient medical histories.


Table of Contents
Features
Technologies Used
Installation
Usage
Project Structure
Models Overview
Contributing
License

Features
User Roles: Separate dashboards for Doctors and Patients.
Appointment Booking: Patients can view doctor availability and book appointments.
Doctor Availability Management: Doctors can set their availability days and time slots.
Medical Records and Prescriptions: Doctors can add medical records and prescriptions, accessible to patients.
Notifications: System notifications for appointments and updates.
Secure Authentication: User registration and login with role-based redirects.
User Profiles: Patients can view and update their profile information.
Technologies Used
Backend: Django (Python)
Database: SQLite (configurable to PostgreSQL/MySQL for production)
Frontend: HTML, CSS, Bootstrap, JavaScript (for interactivity)
Other Libraries: Django REST Framework (for APIs, if applicable), Django Forms for data entry
Installation
Prerequisites
Python 3.8+
Django 4.x
Virtual environment (recommended)
Steps
Clone the Repository

bash
Copy code
git clone https://github.com/Hussnain46/healthcare-management-system.git
cd healthcare-management-system
Set up Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Run Migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser

bash
Copy code
python manage.py createsuperuser
Run the Server

bash
Copy code
python manage.py runserver
Access the Application Open http://127.0.0.1:8000 in your browser.

Usage
Doctor Dashboard

View and update availability.
View and confirm appointment requests.
Add medical records and prescriptions for patients.
Patient Dashboard

View profile and update information.
Book appointments by selecting doctors and available slots.
Access medical records and prescriptions.
Project Structure
plaintext
Copy code
healthcare-management-system/
├── appointments/         # Appointment app
├── medical_records/      # Medical records and prescriptions
├── user/                 # User app (Doctor & Patient management)
├── templates/            # HTML templates
├── healthcare/           # Main project settings
├── static/               # Static files (CSS, JS)
└── README.md             # Project documentation
Models Overview
User (AbstractUser)

Shared fields for all users.
Doctor: Includes specialization, qualifications, and availability.
Patient: Includes date of birth, blood group, and emergency contact.
Appointment

Fields for date, time, patient, doctor, and status (Pending, Confirmed).
Medical Record

Tracks diagnoses, treatments, and is linked to a patient and doctor.
Prescription

Contains medication details, dosage, and doctor-patient association.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new feature branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add a new feature").
Push to the branch (git push origin feature-branch).
Create a Pull Request.
License
This project is licensed under the MIT License.