# Productivity App API

A Flask RESTful API for a Productivity App that allows users to register, log in, and manage personal notes securely.

---

## Features

- User Registration
- User Login
- User Logout
- User Authentication using Sessions
- Create Notes
- View All Notes
- View a Single Note
- Update Notes
- Delete Notes
- Password Hashing using Flask-Bcrypt
- SQLite Database
- Flask-Migrate Database Migrations

---

## Technologies Used

- Python 3.12
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask Bcrypt
- SQLAlchemy
- Marshmallow
- SQLite
- Pipenv

---

## Project Structure

```
productivity-app/
│
├── app.py
├── config.py
├── models.py
├── schemas.py
├── seed.py
├── Pipfile
├── README.md
├── instance/
│   └── app.db
├── migrations/
└── routes/
    ├── auth.py
    └── notes.py
```

---

## Installation

Clone the repository

```bash
git clone <your-github-link>
```

Navigate into the project

```bash
cd productivity-app
```

Install dependencies

```bash
pipenv install
```

Activate the virtual environment

```bash
pipenv shell
```

---

## Database Setup

Initialize migrations

```bash
flask --app app db init
```

Create a migration

```bash
flask --app app db migrate -m "Initial migration"
```

Apply migrations

```bash
flask --app app db upgrade
```

(Optional) Seed the database

```bash
python seed.py
```

---

## Running the Server

```bash
python app.py
```

The application runs at

```
http://127.0.0.1:5555
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /signup | Register a new user |
| POST | /login | Login |
| GET | /me | Get current user |
| DELETE | /logout | Logout |

---

### Notes

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /notes | Get all notes |
| GET | /notes/<id> | Get one note |
| POST | /notes | Create a note |
| PATCH | /notes/<id> | Update a note |
| DELETE | /notes/<id> | Delete a note |

---

## Sample Signup Request

```json
{
    "username": "john",
    "password": "12345"
}
```

---

## Sample Create Note Request

```json
{
    "title": "Shopping List",
    "content": "Buy milk, eggs and bread"
}
```

---

## Author

Lyndsey Isoe

Moringa School Software Engineering Student

---

## License

This project is for educational purposes.