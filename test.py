import unittest
from app import app  # Assuming your Flask app is in a file named app.py
import os

class TestMyApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ToDo Reminder', response.data)

    # Add more test cases as needed

if __name__ == '__main__':
    with open('reports/test_results.xml', 'wb') as output:
        runner = unittest.TextTestRunner(output=output)
        unittest.main(testRunner=runner)
