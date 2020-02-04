"""
Module contains http Method (Get,Post,update(put),delete)
"""
import click
from ..parent_command import parent
from ..httpmethoddefinationpackage.http_method_implementation import RestApiCli


RESTCLIOBJ = RestApiCli()   # object of RestApiMethodImplementatio object to call restapi method


@parent.command(help='This is command for HttpGet method')
@click.argument('url')
def http_get(url):
    '''
    http_get is subcommand
    '''
    click.echo(RESTCLIOBJ.get_method_response(url))


@parent.command(help='This is command for HttpPost method ..Please send data in json format for post request')
@click.argument('url')
@click.argument('json_data')
def http_post(url, json_data):
    '''
    http_post is subcommand
    '''
    click.echo(RESTCLIOBJ.post_method_response(url, json_data))


@parent.command(help='This is command for http put method')
@click.argument('url')
@click.argument('json_data')
def http_put(url, json_data):
    '''
    http-put is usbcommand
    '''
    click.echo(RESTCLIOBJ.put_method_response(url, json_data))


@parent.command(help='This is command for http delete method')
@click.argument('url')
def http_delete(url):
    '''
    http-delete is subcommand
    '''
    click.echo(RESTCLIOBJ.delete_method(url))
