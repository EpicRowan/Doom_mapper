
from sqlalchemy import func

from model_project import SoftStory, connect_to_db, db

from server import app

def load_buildings(soft_filename, tall_filename):
    """Load users from u.user into database."""
   print("Buildings")


    for i, row in enumerate(open(soft_filename)):
        row = row.rstrip()
        property_address, status = row.split(",")


        building= Building(property_address= address)


        db.session.add(building)

         if i % 100 == 0:
            print(i)

    for i, row in enumerate(open(tall_filename)):
        row = row.rstrip()
        name, address, at_risk, liquefaction = row.split(",")

        building= Building(property_address= address)


        db.session.add(building)

         if i % 100 == 0:
            print(i)
    # Once we're done, we should commit our work
    db.session.commit()


def load_soft_story_status(soft_filename):
    """Load users from u.user into database."""

    print("Soft-Story Buildings")

    for i, row in enumerate(open(soft_filename)):
        row = row.rstrip()
        property_address, status = row.split(",")

        soft_story = SoftStory(status=status)

        # We need to add to the session or it won't ever be stored
        db.session.add(soft_story)

    # Once we're done, we should commit our work
    db.session.commit()

def load_tall_building(tall_filename):
    """Load users from u.user into database."""

    print("Tall Buildings")

    for i, row in enumerate(open(tall_filename)):
        row = row.rstrip()
        name, address, at_risk, liquefaction = row.split(",")

        tall_building = TallBuilding(name=name, liquefaction=liquefaction, at_risk = at_risk)

        # We need to add to the session or it won't ever be stored
        db.session.add(tall_building)

    # Once we're done, we should commit our work
    db.session.commit()



# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    soft_filename = "seed_data/Soft-Story_Properties_clean.csv"
    tall_filename = "seed_data/Tall_Building_Inventory_clean.csv"
    load_buildings(soft_filename, tall_filename)
    load_soft_story_status(soft_filename)
    load_tall_building(tall_filename)
    # set_val_user_id()