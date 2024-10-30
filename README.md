<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Healthcare Management System</h1>

<p>A comprehensive web-based Healthcare Management System built with Django, designed to streamline medical appointment booking, prescription management, and medical record tracking for patients and healthcare providers. This project includes secure user management, customizable appointment scheduling, and easy access to patient medical histories.</p>

<h2>Table of Contents</h2>
<ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#models-overview">Models Overview</a></li>
    <li><a href="#contributing">Contributing</a></li>
</ol>

<h2 id="features">Features</h2>
<ul>
    <li><strong>User Roles</strong>: Separate dashboards for Doctors and Patients.</li>
    <li><strong>Appointment Booking</strong>: Patients can view doctor availability and book appointments.</li>
    <li><strong>Doctor Availability Management</strong>: Doctors can set their availability days and time slots.</li>
    <li><strong>Medical Records and Prescriptions</strong>: Doctors can add medical records and prescriptions, accessible to patients.</li>
    <li><strong>Secure Authentication</strong>: User registration and login with role-based redirects.</li>
    <li><strong>User Profiles</strong>: Patients can view and update their profile information.</li>
</ul>

<h2 id="technologies-used">Technologies Used</h2>
<ul>
    <li><strong>Backend</strong>: Django (Python)</li>
    <li><strong>Database</strong>: SQLite3</li>
    <li><strong>Frontend</strong>: HTML, CSS, Bootstrap, JavaScript (for interactivity)</li>
    <li><strong>Other Libraries</strong>:Django Forms for data entry</li>
</ul>

<h2 id="installation">Installation</h2>
<h3>Prerequisites</h3>
<ul>
    <li>Python 3.8+</li>
    <li>Django 5.1.1</li>
    <li>Virtual environment (recommended)</li>
</ul>

<h3>Steps</h3>
<ol>
    <li><strong>Clone the Repository</strong>
        <pre><code>git clone https://github.com/Hussnain46/Healthcare-Management-System.git
cd Healthcare-Management-System</code></pre>
    </li>
    <li><strong>Set up Virtual Environment</strong>
        <pre><code>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`</code></pre>
    </li>
    <li><strong>Install Dependencies</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Run Migrations</strong>
        <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>
    </li>
    <li><strong>Create a Superuser</strong>
        <pre><code>python manage.py createsuperuser</code></pre>
    </li>
    <li><strong>Run the Server</strong>
        <pre><code>python manage.py runserver</code></pre>
    </li>
    <li><strong>Access the Application</strong>
        Open <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a> in your browser.
    </li>
</ol>

<h2 id="usage">Usage</h2>
<ol>
    <li><strong>Doctor Dashboard</strong>
        <ul>
            <li>View and update availability.</li>
            <li>View and confirm appointment requests.</li>
            <li>Add medical records and prescriptions for patients.</li>
        </ul>
    </li>
    <li><strong>Patient Dashboard</strong>
        <ul>
            <li>View profile and update information.</li>
            <li>Book appointments by selecting doctors and available slots.</li>
            <li>Access medical records and prescriptions.</li>
        </ul>
    </li>
</ol>



<h2 id="models-overview">Models Overview</h2>
<ol>
    <li><strong>User (AbstractUser)</strong>
        <ul>
            <li>Shared fields for all users.</li>
            <li><strong>Doctor</strong>: Includes specialization, qualifications, and availability.</li>
            <li><strong>Patient</strong>: Includes date of birth, blood group, and emergency contact.</li>
        </ul>
    </li>
    <li><strong>Appointment</strong>
        <ul>
            <li>Fields for date, time, patient, doctor, and status (Pending, Confirmed).</li>
        </ul>
    </li>
    <li><strong>Medical Record</strong>
        <ul>
            <li>Tracks diagnoses, treatments, and is linked to a patient and doctor.</li>
        </ul>
    </li>
    <li><strong>Prescription</strong>
        <ul>
            <li>Contains medication details, dosage, and doctor-patient association.</li>
        </ul>
    </li>
</ol>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! Please follow these steps:</p>
<ol>
    <li>Fork the repository.</li>
    <li>Create a new feature branch (<code>git checkout -b feature-branch</code>).</li>
    <li>Commit your changes (<code>git commit -m "Add a new feature"</code>).</li>
    <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
    <li>Create a Pull Request.</li>
</ol>


</body>
</html>
