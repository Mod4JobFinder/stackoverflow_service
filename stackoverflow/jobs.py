from flask import Flask, request
import requests
import json
import xmltodict
import html
import re
import operator
from datetime import datetime
from collections import OrderedDict
def create_app():
  app = Flask(__name__)

  @app.route("/api/v1/jobs")
  def jobs():
    get_params = request.args
    params = {'q': get_params.get('title'), 'l': get_params.get('location')}
    req = requests.get("https://stackoverflow.com/jobs/feed", params=params)
    to_json = xmltodict.parse(req.content)
    cleaned = html.unescape(to_json)
    data = json.dumps(cleaned)
    json_raw = json.loads(data)
    results = json_raw["rss"]["channel"]["item"]
    final_json_raw = json.dumps(job_data(results), indent = 4)
    final_json = json.loads(final_json_raw)

    return final_json

  def job_data(results):
    job_data = {'data': []}
    for job in results:
      updated_time = datetime.strptime(job['pubDate'][:-2],'%a, %d %b %Y %H:%M:%S' )
      job.update({'pubDate': updated_time})
    results.sort(key = operator.itemgetter('pubDate'), reverse = True)
    top_40 = results[:40]
    for job in top_40:
      job_data['data'].append(create_job(job))
    return job_data

  def create_job(job):
    return OrderedDict({
    'id': job['guid']['#text'],
    'type': 'job_post',
    'attributes': {
      'title': job['title'],
      'company': job['a10:author']['a10:name'],
      'category': job.get('category'),
      'description': clean_description(job),
      'location': job['location']['#text'],
      'publish_date': datetime.strftime(job['pubDate'], '%c'),
      'link': job['link']
    }
    })

  def clean_description(job):
      breaks = re.compile("<br />")
      clean = re.compile("<.*?>")
      symbol_1 = re.compile("&amp;")
      apostrophies = re.compile("&rsquo;")
      em_dashes = re.compile("&ndash;")
      clean_breaks = re.sub(breaks, "**BREAK** ", job['description'])
      clean_symbol_1 = re.sub(symbol_1, "&", clean_breaks)
      clean_apostrophies = re.sub(apostrophies, "'", clean_symbol_1)
      clean_em_dashes = re.sub(em_dashes, "–", clean_apostrophies)
      description = re.sub(clean, "", clean_em_dashes)
      return description
      
  return app