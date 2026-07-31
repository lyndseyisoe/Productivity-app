from config import app, db
from models import User, Note

with app.app_context():
    # Clear existing data
    Note.query.delete()
    User.query.delete()

    # Create users
    user1 = User(username="alice")
    user1.password = "password123"

    user2 = User(username="bob")
    user2.password = "password123"

    db.session.add_all([user1, user2])
    db.session.commit()

    # Create notes
    note1 = Note(
        title="Shopping List",
        content="Milk, Bread, Eggs",
        user_id=user1.id
    )

    note2 = Note(
        title="Homework",
        content="Finish Flask project",
        user_id=user1.id
    )

    note3 = Note(
        title="Meeting",
        content="Project meeting at 2 PM",
        user_id=user2.id
    )

    db.session.add_all([note1, note2, note3])
    db.session.commit()

    print("Database seeded successfully!")