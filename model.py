"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions

class Building(db.Model):
    """Main building data table of all known buildings."""

    __tablename__ = "buildings"

    building_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    address = db.Column(db.String(64), nullable=False)

    latitude = db.Column(db.String(64), nullable=True)

    longitude = db.Column(db.String(64), nullable=True)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Building ID={self.building_id} Address={self.address}>"

class SoftStory(db.Model):
    """Status of retrofitted or non-compliant for soft story buildings."""

    __tablename__ = "softstories"

    ss_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)

    building_id = db.Column(db.Integer,
                        db.ForeignKey("buildings.building_id"),
                        unique=True)

    status = db.Column(db.String(64), nullable=True)

    liquefaction = db.Column(db.String(), nullable=True)

    building = db.relationship('Building', backref=db.backref('softstory', uselist=False))
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Soft Story Id={self.ss_id} Status={self.status}>"

class TallBuilding(db.Model):
    """Info about the liquefaction and construction risks of tall buildings in SF."""

    __tablename__ = "tallbuildings"

    tall_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)

    building_id = db.Column(db.Integer,
                        db.ForeignKey("buildings.building_id"),
                        unique=True)

    name = db.Column(db.String(64), nullable=True)

    liquefaction = db.Column(db.String(64), nullable=True)

    at_risk = db.Column(db.Boolean(), nullable=True)

    building = db.relationship('Building', backref=db.backref('tallbuilding', uselist=False))
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Tall Building ID={self.tall_id} Liquefaction={self.liquefaction}>"



# #####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///buildings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
