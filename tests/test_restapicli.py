"""
This is unittest module 
"""

import unittest
from unittest.mock import patch


class TestRestAPICli(unittest.TestCase):
    """"
    Unit test case for httpMethod
    """
    HOST = '127.0.0.1'
    PORT = '8000'
    ENDPOINT = ''

    def setUp(self):
        self.base_url = f'http://{self.HOST}:{self.PORT}/{self.ENDPOINT}/'

    @patch('src.httpmethoddefinationpackage.http_method_implementation.RestApiCli')
    def test_get_method_response(self, MockRestApiCli):
        """
        this is mocking test to check get_method_response
        """
        restapicliobj = MockRestApiCli()
        restapicliobj.get_method_response.return_value = 200
        actual = restapicliobj.get_method_response(self.base_url)
        expected = 200
        self.assertEqual(expected, actual)

    @patch('src.httpmethoddefinationpackage.http_method_implementation.RestApiCli')
    def test_post_method_response(self, MockRestAPICli):
        """
        this is mocking test to check post_method_response
        """
        restapicliobj = MockRestAPICli()
        restapicliobj.post_method_response.return_value = 200
        actual = restapicliobj.post_method_response(self.base_url, {'Key': 'value'})
        expected = 200
        self.assertEqual(expected, actual)

    @patch('src.httpmethoddefinationpackage.http_method_implementation.RestApiCli')
    def test_put_method_response(self, MockRestAPICli):
        """
        this is mocking test to check put_method_response
        """
        restapicliobj = MockRestAPICli()
        restapicliobj.put_method_response.return_value = 200
        actual = restapicliobj.put_method_response(self.base_url, {'Key': 'value'})
        expected = 200
        self.assertEqual(expected, actual)

    @patch('src.httpmethoddefinationpackage.http_method_implementation.RestApiCli')
    def test_delete_method(self, MockRestAPICli):
        """
        this is mocking test to check delete_method
        """
        restapicliobj = MockRestAPICli()
        restapicliobj.delete_method.return_value = 200
        actual = restapicliobj.delete_method(self.base_url)
        expected = 200
        self.assertEqual(expected, actual)
