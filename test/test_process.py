import unittest
from modules.process import extract_authorscreen, extract_authordate, extract_authorname, \
    extract_messageid, extract_authorid, extract_messagedata, extract_messagedate
from data_example import data


class ProcessingTest(unittest.TestCase):
    """Test for process.py"""

    def test_extract_messageid(self):
        self.assertEqual(1, extract_messageid(data))

    def test_extract_messagedata(self):
        self.assertEqual('text', extract_messagedata(data))

    def test_extract_messagedate(self):
        self.assertEqual(1611071438.0, extract_messagedate(data))

    def test_extract_authorscreen(self):
        self.assertEqual("screen_name", extract_authorscreen(data))

    def test_extract_authorname(self):
        self.assertEqual("name", extract_authorname(data))

    def test_extract_authorid(self):
        self.assertEqual(1, extract_authorid(data))

    def test_extract_authordate(self):
        self.assertEqual(1588778777.0, extract_authordate(data))
        # data['user_loc'] = tweet['user']['location']


if __name__ == '__main__':
    unittest.main()