"""
This is moduel of parent command
"""
import click


@click.group()
def parent():
    """
    sham-restapicli is Parent command for RestAPI CLI \n
    sham-restapicli http-get is need one url of api \n
    sham-restapicli http-post is need two argument url and data in dictionary formate

    """
    pass
