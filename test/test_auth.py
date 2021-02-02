import unittest
from modules.auth import openfile
import os


class TestAuth(unittest.TestCase):

    def test_openfile(self):
        credentials = openfile(os.path.join(os.path.dirname(__file__), "credentials_example.json"))
        self.assertTrue("CONSUMER_KEY" == credentials[0])
        self.assertTrue("CONSUMER_SECRET" == credentials[1])
        self.assertTrue("ACCESS_TOKEN" == credentials[2])
        self.assertTrue("ACCESS_SECRET" == credentials[3])


if __name__ == '__main__':
    unittest.main()
