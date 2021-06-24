<h1 align='center'>StackOverflow Microservice</h1>
The Stackoverflow Microservice utilizes an RSS feed from StackOverflow Jobs to expose a job data API for the Back End Job Finder Application.

## Versioning
- Python 3.9.5
- Pytest 6.2.4
- Flask 2.0.0

## Getting Started
1. Fork and Clone this repository
2. Run `pipenv install` to ensure packages are installed in your environment
3. Run `pytest` to run this app's tests to ensure it is working correctly
4. To run this application locally, run `gunicorn run:app` and follow the given address

## Endpoints
### StackOverflow Microservice to Backend

**Required** path params:
- `location`
- `title`

*will return 404 if not provided*

GET '/api/v1/jobs?location=denver,co&title=software+engineer
> ```
> {
>  "data": [{
>    "id": "integer",
>    "type": "job_post",
>    "attributes":{
>      "title": "string",
>      "company": "string",
>      "category": "array(strings)",
>      "description": "string",
>      "location": "string",
>      "publish_date": "datetime",
>      "link": "string"
>      },
>      {...}
>   }]
> }
