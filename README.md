# Flask Notes App

A secure and user-friendly Notes Management web application built with **Flask**. The application allows users to register, log in, and manage their personal notes with full CRUD (Create, Read, Update, Delete) functionality.

---

##  Features

-  User Registration
-  Secure Login & Logout
-  Password Hashing using Werkzeug
-  Create New Notes
-  Edit Existing Notes
-  Delete Notes
-  View Personal Dashboard
-  Flash Messages for User Feedback
-  Session-Based Authentication
-  SQLite Database Integration
-  Simple REST API Endpoint (`/notes`)

---

##  Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Flask | Backend Framework |
| Flask-SQLAlchemy | ORM |
| SQLite | Database |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive UI |
| Jinja2 | Template Engine |
| Werkzeug | Password Hashing & Security |

---

##  Project Structure

```text
notes_app/
│
├── instance/
│   └── notes.db
│
├── routes/
│   ├── auth.py
│   ├── notes.py
│   └── api.py
│
├── static/
│   └── css/
│       └── styles.css
│
├── templates/
│   ├── index.html
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_note.html
│   └── edit_note.html
│
├── app.py
├── config.py
├── extensions.py
├── models.py
├── requirements.txt
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

### 2. Navigate into the project

```bash
cd <repository-name>
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000/
```

---

##  Available Routes

| Route | Description |
|--------|-------------|
| `/` | Home Page |
| `/register` | User Registration |
| `/login` | User Login |
| `/logout` | Logout |
| `/dashboard` | User Dashboard |
| `/add_note` | Add a Note |
| `/edit_note/<note_id>` | Edit Note |
| `/delete_note/<note_id>` | Delete Note |
| `/notes` | REST API Endpoint |

---

##  Authentication

- Passwords are securely hashed before being stored.
- Users can only view and manage their own notes.
- Session management is used to keep users logged in.
- Unauthorized users are redirected to the login page.

---

##  Database

This project uses **SQLite** with **Flask-SQLAlchemy**.

Two database models are included:

### User

- ID
- Username
- Email
- Password (Hashed)

### Note

- ID
- Title
- Description
- User ID (Foreign Key)

---

##  Future Improvements

- Search Notes
- Categories & Tags
- Note Pinning
- Rich Text Editor
- Dark Mode
- Profile Management
- Pagination
- REST API Authentication (JWT)
- Responsive Mobile UI
- Note Sharing

---

##  Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- Werkzeug

Install using:

```bash
pip install -r requirements.txt
```

---

##  Author

**Sakthi Mageswari V**

Computer Science Engineering Student

GitHub: https://github.com/Sakthi-05
