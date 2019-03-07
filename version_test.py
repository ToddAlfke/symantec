import sys
from elasticsearch import Elasticsearch
from elasticsearch import Elasticsearch,helpers
from elasticsearch.helpers import scan
sys.path.append('/home/ubuntu/')
from ElasticsearchConfig import *
#################################

es = Elasticsearch(ElasticsearchIP)

#################################


list_id = helpers.scan(es,query={"query":{"match_all": {}}},scroll='1m',index='packetstormsecurity', doc_type="items")
IDs = [item_id['_id'] for item_id in list_id]
for item_id in IDs:
    res = es.get(index='packetstormsecurity', doc_type='items', id=item_id)
    version = (res["_version"])
    source = (res["_source"])
#    if version == 1:
    print(version)


################  TESTING  ################
#def project():
#    list_id = helpers.scan(es,query={"query":{"match_all": {}}},scroll='1m',index='project', doc_type="items")
#    IDs = [item_id['_id'] for item_id in list_id]
#    for item_id in IDs:
#        res = es.get(index=project, doc_type='items', id=item_id)
#        version = (res["_version"])
#        version_check = 7
#        source = (res["_source"])
#        if version == version_check:
#           print(source)
#
#project()

################  TESTING  ################
#Projects = ['packetstormsecurity', 'netsparker']
#
#for project in Projects:
#    list_id = helpers.scan(es,query={"query":{"match_all": {}}},scroll='1m',index=project, doc_type="items")
#    IDs = [item_id['_id'] for item_id in list_id]
#    for item_id in IDs:
#        res = es.get(index=project, doc_type='items', id=item_id)
#        version = (res["_version"])
#        version_check = 1
#        source = (res["_source"])
#        if version == version_check:
#           print(source)


##################  THIS BLOCK OF CODE CALLS THE DOCUMENT TYPE FOR ID  ###################################

#a = es.get(index="packetstormsecurity", doc_type='items', id='466cdc1caa1df263d9309b2595cde2e4691d9047')
#version=['_id']
#print(version)
#print(res)

##########################################################################################################



##################  THIS BLOCK OF CODE CREATES A LIST FOR ALL /INDEX/TYPE/ID's  #############################
#############################################################################################################

#a=helpers.scan(es,query={"query":{"match_all": {}}},scroll='1m',index="packetstormsecurity", doc_type="items")
#IDs=[aa['_id'] for aa in a]
#print(IDs)

#############################################################################################################
