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
  response = client.get("/jobs?location=denver,co&position=software+engineer")
  assert response.status_code == 200

  
