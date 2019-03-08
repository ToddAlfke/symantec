import sys
import smtplib
#import re
#import glob
from elasticsearch import Elasticsearch
from elasticsearch import Elasticsearch,helpers
from elasticsearch.helpers import scan
from ElasticsearchConfig import *
#################################

es = Elasticsearch(ElasticsearchIP)

#################################


################  TESTING  ################
#Projects = glob.glob('site-source/*')
Projects = ['packetstormsecurity', 'netsparker']
#def getUpdate():
for project in Projects:
    list_id = helpers.scan(es,query={"query":{"match_all": {}}},scroll='1m',index=project, doc_type="items")
    IDs = [item_id['_id'] for item_id in list_id]
    for item_id in IDs:
        res = es.get(index=project, doc_type='items', id=item_id)
        version = (res["_version"])
        source = (res["_source"])
        if version == 7:
           print(source)
#getUpdate()
#message = str(getUpdate)

#server = smtplib.SMTP('smtp.gmail.com', 587)
#server.starttls()
#server.login("todd.alfke@gmail.com", "")


#msg = message
#server.sendmail("todd.alfke@gmail.com", "todd.alfke@gmail.com", msg)
#server.quit()
