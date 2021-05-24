import pytest

from stackoverflow.jobs import create_app

@pytest.fixture
def app():
  app = create_app()

  app.testing = True

  return app

@pytest.fixture
def client(app):
  client = app.test_client()
  return client


def test_jobs_has_successful_response(client):
  response = client.get("/api/v1/jobs?location=denver,co&position=software+engineer")
  assert response.status_code == 200

def test_jobs_has_data_key(client):
  response = client.get("/api/v1/jobs?location=denver,co&position=software+engineer")
  body = response.json
  assert 'data' in body.keys()
  
  data = body['data']

  assert 'id' in data.keys()
  assert 'type' in data.keys()
  assert 'attributes' in data.keys()


  
