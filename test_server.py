
import unittest 
import server

class TestFlaskRoutes(unittest.TestCase):
    """Test Flask routes."""

    def test_home(self):
        """Make sure home page returns correct HTML."""

        client = server.app.test_client()
        server.app.config['TESTING'] = True
        result = client.get('/')

        self.assertEqual(result.status_code, 200)

    # def test_home(self):
    #     """Make sure home page returns correct HTML."""

    #     client = server.app.test_client()
    #     server.app.config['TESTING'] = True
    #     result = client.get('/')
        
    #     self.assertEqual(result.status_code, 200)






if __name__ == '__main__':
	unittest.main()