from .models import Job, db, connect_db, refresh_db, serialize_job
from flask import Flask, cli, request, jsonify
from flask_cors import CORS
import os
from .scraping import find_monster_jobs, find_stepstone_jobs

# creating the Flask application
app = Flask(__name__)

# activate CORS for flask app
CORS(app)

# load .env variables
cli.load_dotenv(".env")

# get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URI", "postgres:///jobbig")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "secret123")

connect_db(app)
db.create_all()


@app.route("/", methods=["GET"])
def awake():
    """ Wake up the server on Heroku """
    return "I am awake"


@app.route("/stepstone", methods=["GET"])
def get_stepstone():
    """ Get jobs from Stepstone """

    refresh_db("stepstone")

    title = request.args.get("title")
    city = request.args.get("city")
    stepstone_jobs = find_stepstone_jobs(title, city)

    for item in stepstone_jobs:
        job = Job(
            title=item["title"],
            company=item["company"],
            location=item["location"],
            url=item["url"],
            source="stepstone",
        )
        db.session.add(job)

    db.session.commit()

    jobs = Job.query.filter_by(source="stepstone").all()

    serialized = [serialize_job(j) for j in jobs]

    return jsonify(serialized)


@app.route("/monster", methods=["GET"])
def get_monster():
    """ Get jobs from Monster """

    refresh_db("monster")

    title = request.args.get("title")
    city = request.args.get("city")
    monster_jobs = find_monster_jobs(title, city)

    for item in monster_jobs:
        job = Job(
            title=item["title"],
            company=item["company"],
            location=item["location"],
            url=item["url"],
            source="monster",
        )
        db.session.add(job)

    db.session.commit()

    jobs = Job.query.filter_by(source="monster").all()

    serialized = [serialize_job(j) for j in jobs]

    return jsonify(serialized)