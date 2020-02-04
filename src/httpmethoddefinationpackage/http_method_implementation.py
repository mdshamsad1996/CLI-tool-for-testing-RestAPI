"""
Module conatins defination of all http method using request library
"""
import requests
import click
from requests.exceptions import HTTPError


class RestApiCli:
    '''
    RestAPI Method  implementation

    '''
    def get_method_response(self, url):
        '''
        Get response  using given url
        '''
        try:
            response = requests.get(url)
            click.echo(response.json())
            # If the response was successful, no Exception will be raised
            response.raise_for_status()

        except HTTPError as http_err:
            return f'HTTP error occurred: {http_err}'

        except Exception as err:
            return f'Other error occurred: {err}'

        else:
            return 'Success!'

    def post_method_response(self, url, json_data):
        '''
        Http Post implementation
        '''
        try:
            headers = {'content-type': 'application/json', 'Accept': 'text/plain'}
            response = requests.post(url, data=json_data, headers=headers)
            click.echo(response.json())
            response.raise_for_status()

        except HTTPError as http_err:
            return f'HTTP error occured: {http_err}'

        except Exception as err:
            return f'other error occured:{err}'

        else:
            return 'Success!'

    def put_method_response(self, url, json_data):
        '''
        HttP Put method

        '''
       
        try:
            headers = {'content-type': 'application/json', 'Accept': 'text/plain'}
            response = requests.put(url, data=json_data, headers=headers)
            click.echo(response)
            response.raise_for_status()

        except HTTPError as http_err:
            return f'Http error occured: {http_err}'
        except Exception as err:
            return f'other error occured: {err}'
        else:
            return 'Success!'

    def delete_method(self, url):
        ''''
        Http delete method
        '''
        try:
            # headers = {'content-type': 'application/json', 'Accept': 'text/plain'}
            response = requests.delete(url)
            click.echo(response.json())
            response.raise_for_status()
        except HTTPError as http_err:
            return f'Http error occured: {http_err}'
        except Exception as err:
            return f'other error occured:{err}'
        else:
            return 'Succes!'
