
import unittest 
from server import app 
from model import db, connect_to_db, example_data




class TestFlaskRoutes(unittest.TestCase):
    """Test Flask routes."""

    def setUp(self):
      """Stuff to do before every test."""

      self.client = app.test_client()
      app.config['TESTING'] = True

      # Connect to test database
      connect_to_db(app,"postgresql:///testdb")

      # Create tables and add sample data
      db.create_all()
      example_data()

    def tearDown(self):
    	"""Stuff to do after each test."""

    def test_home(self):
        """Make sure home page returns correct HTML."""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_tall_api(self):
        """Test tall api."""

        result = self.client.get("/api/tallbuildings")

        self.assertIn(b'MegaCorp', result.data)

    def test_softstory_api(self):
        """Test softstory api"""

        result = self.client.get("/api/softbuildings")

        self.assertIn(b"123 Fake st", result.data)

    def test_building_id_search(self):
        """Test BID search."""

        result = self.client.get("/buildings/1")

        self.assertIn(b"<title>Doom Mapper</title>", result.data)


    def test_search(self):
        """Test search."""

        result = self.client.get("/search", query_string={"entered_address":'123 Fake st'})

        self.assertIn(b"<title>Doom Mapper</title>", result.data)




if __name__ == '__main__':
	unittest.main()
	# connect_to_db(app)

