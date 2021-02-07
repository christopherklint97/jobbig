"""SQLAlchemy models for Jobbig."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """ Users in the app """

    __tablename__ = "users"

    id = db.Column(
        db.String(200),
        primary_key=True,
    )

    email = db.Column(db.String(200), nullable=False)


class Job(db.Model):
    """ Jobs are jobs """

    __tablename__ = "jobs"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    title = db.Column(db.String(200), nullable=False)

    company = db.Column(db.String(200), nullable=False)

    location = db.Column(db.String(200), nullable=False)

    url = db.Column(db.String(200), nullable=False)

    source = db.Column(db.String(200), nullable=False)

    future_id = db.Column(
        db.Integer, db.ForeignKey("futures.id", ondelete="cascade"), nullable=False
    )

    future = db.relationship("Future", backref="jobs")


class Future(db.Model):
    """ Futures are lists of job ads """

    __tablename__ = "futures"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(db.String(200), nullable=False)

    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="cascade"), nullable=False
    )

    user = db.relationship("User", backref="futures")


def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)