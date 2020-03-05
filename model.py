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
    """Status of retrofitted or non-compliant and liquefaction risk for soft story buildings."""

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


def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    SoftStory.query.delete()
    TallBuilding.query.delete()
    Building.query.delete()

    print('example_data')

    # Sample Building table

    B1 = Building(building_id =1, address='123 Fake st', latitude ="37.799302431542", longitude="-122.406357955549")
    B2 = Building(building_id =2, address='456 Fake st', latitude ="37.799302431542", longitude="-122.406357955549")
    B3 = Building(building_id =3, address='2 Narnia way', latitude ="37.799302431542", longitude="-122.406357955549")
    B4 = Building(building_id =4, address='1 Right way', latitude ="37.799302431542", longitude="-122.406357955549")
    B5 = Building(building_id =5, address='2 Wrong way', latitude ="37.799302431542", longitude="-122.406357955549")
    B6 = Building(building_id =6, address='3 Hacker Street', latitude ="37.799302431542", longitude="-122.406357955549")

    # Sample tall buildings

    T1 = TallBuilding(building_id =1, name='MegaCorp', liquefaction='Very High', at_risk= True)
    T2 = TallBuilding(building_id =2, name='JumboCorp', liquefaction='Very Low', at_risk= False)
    T3 = TallBuilding(building_id =3, name='GodzillaCorp', liquefaction='Moderate', at_risk= True)

    # Sample soft story buildings

    S1 = SoftStory(building_id=4, status="Seismic Retrofitted", liquefaction= "yes")
    S2 = SoftStory(building_id=5, status="Seismic Retrofitted", liquefaction= "yes")
    S3 = SoftStory(building_id=6, status="Non-Compliant", liquefaction= "yes")
    

    db.session.add_all([B1, B2, B3, B4, B5, B6, T1, T2, T3, S1, S2, S3])
    db.session.commit()    

    print(TallBuilding.query.all(),Building.query.all(), SoftStory.query.all())


# #####################################################################
# Helper functions

def connect_to_db(app, db_name="postgresql:///buildings"):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_name
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
