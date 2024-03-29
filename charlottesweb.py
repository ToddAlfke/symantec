#### ##################################################
import subprocess
import glob
from elasticsearch import Elasticsearch
from ElasticsearchConfig import *

### Import from ElasticsearchConfig Modlue ElasticsearchIP
### Check Connection to Elastisearch and run subprocess for each scrapy charlotte spider ###
es = Elasticsearch(['http://'+ElasticsearchIP+':9200/'], verify_certs=True)
if not es.ping():
    print('Failed configuration for %s' % es)
    raise ValueError("Connection to Elasticsearch failed. Update Elasticsearch configuration and try again.")
elif es.ping():
    for project in glob.glob('site-source/*'):
        subprocess.call('scrapy crawl charlotte', shell=True, cwd=project)
