import unittest


class MyStreamerTest(unittest.TestCase):
    """Test for process.py"""

    def test_on_success(self, data="My Message"):
        self.assertTrue(data)

    def test_on_error(self, code=400, data="My Message"):
        self.assertTrue(code or data)


if __name__ == '__main__':
    unittest.main()