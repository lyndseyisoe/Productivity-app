from config import app

# Import models so Flask-Migrate can detect them
from models import User, Note

from routes.auth import auth_bp
from routes.notes import notes_bp

app.register_blueprint(auth_bp)
app.register_blueprint(notes_bp)

if __name__ == "__main__":
    app.run(port=5555, debug=True)