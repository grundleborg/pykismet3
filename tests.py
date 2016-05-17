import unittest

from pykismet3 import Akismet, ExtraParametersError


'''
PykismetTestCase

- tests for pykismet3 package
- requires python requests module in order to run (pip install requests)

'''

class PykismetTestCase(unittest.TestCase):

    # create an instance of the Akismet class
    def setUp(self):

        self.akismet_client = Akismet(blog_url="http://your.blog/url",
                                      user_agent="My Awesome Web App/0.0.1",
                                      api_key="testkey")


    # test that class raises an ExtraParametersError when extra params are passed
    def test_extra_parameters(self):
        params = {'blog': 'http://your.blog/url',
                  'user_ip': '1.1.1.1',
                  'user_agent': 'My Awesome Web App/0.0.1',
                  'referrer': 'http://your.blog/url',
                  'some_extra': 'extra'
                  }

        with self.assertRaises(ExtraParametersError):
            self.akismet_client.check(params)
