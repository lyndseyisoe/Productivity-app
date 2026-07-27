from datetime import datetime

from sqlalchemy.orm import validates

from app import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    notes = db.relationship(
        "Note",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    @property
    def password(self):
        raise AttributeError("Password is not readable.")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    @validates("username")
    def validate_username(self, key, username):
        if not username or not username.strip():
            raise ValueError("Username cannot be empty.")
        return username.strip()

    def __repr__(self):
        return f"<User {self.username}>"


class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    user = db.relationship(
        "User",
        back_populates="notes",
    )

    @validates("title")
    def validate_title(self, key, title):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty.")
        return title.strip()

    @validates("content")
    def validate_content(self, key, content):
        if not content or not content.strip():
            raise ValueError("Content cannot be empty.")
        return content.strip()

    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"