from pytest import fixture

from pyswagger import App
from pyswagger.primitives import MimeCodec
from pyswagger.primitives.codec import JsonCodec
from pyswagger.contrib.client.requests import Client


@fixture
def client():
    client = Client()
    return client


@fixture
def app():
    _codec = MimeCodec()
    _codec.register('application/json', JsonCodec())

    # TODO: how to load .yaml?
    app = App.load('http://petstore.swagger.io/v2/swagger.json', 
                   mime_codec=_codec)
    app.prepare(strict=True)
    return app


