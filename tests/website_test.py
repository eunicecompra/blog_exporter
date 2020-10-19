import unittest

from src import website


class WebsiteTest(unittest.TestCase):
    def test_launch(self):
        self.assertEquals(website.launch("http://www.google.com"), "Google")


if __name__ == '__main__':
    unittest.main()
