"""SQLAlchemy models for Jobbig."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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


def refresh_db(source: str):
    db.session.query(Job).filter(Job.source == source).delete()
    db.session.commit()


def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)