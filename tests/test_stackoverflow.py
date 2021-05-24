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
  response = client.get("/api/v1/jobs?location=denver,co&title=software+engineer")
  assert response.status_code == 200

def test_jobs_has_data_key(client):
  response = client.get("/api/v1/jobs?location=denver,co&title=software+engineer")
  body = response.json
  assert 'data' in body.keys()
  
def test_jobs_have_correct_keys(client):
  response = client.get("/api/v1/jobs?location=denver,co&title=software+engineer")
  body = response.json
  data = body['data']

  for job in data:
    assert 'id' in job.keys()
    assert 'type' in job.keys()
    assert 'attributes' in job.keys()

    assert 'title' in job['attributes'].keys()
    assert 'company' in job['attributes'].keys()
    assert 'category' in job['attributes'].keys()
    assert 'description' in job['attributes'].keys()
    assert 'location' in job['attributes'].keys()
    assert 'publish_date' in job['attributes'].keys()
    assert 'link' in job['attributes'].keys()

def test_404_status_if_no_params_given(client):
  response = client.get("api/v1/jobs")

  assert response.status_code == 404

  
