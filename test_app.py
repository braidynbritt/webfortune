import pytest
import re
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_cowsay(app, client):
    message = 'hello'
    res = client.get('/cowsay/%s/' % message)
    page_output = res.get_data(as_text=True)
    assert message in page_output

def test_fortune(app, client):
    res = client.get('/fortune/')
    page_output = res.get_data(as_text=True)
    assert type(page_output) == str
    assert page_output != ""

def test_cowfortune(app, client):
    res = client.get('/cowfortune/')
    page_output = res.get_data(as_text=True)

    match = re.search('[a-zA-Z]', page_output[5:-1])
    assert match != None
    assert "(oo)" in page_output
