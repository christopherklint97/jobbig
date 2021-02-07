from .models import db, connect_db
from flask import (
    Flask,
    cli,
    jsonify,
)
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from .auth import AuthError, requires_auth
import os

# creating the Flask application
app = Flask(__name__)

# Activate CORS for flask app
CORS(app)

# Load .env variables
cli.load_dotenv(".env")

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URI", "postgres:///jobbig")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "secret123")
toolbar = DebugToolbarExtension(app)

connect_db(app)

db.create_all()


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response