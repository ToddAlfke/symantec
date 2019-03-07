from elasticsearch import Elasticsearch
from elasticsearch import Elasticsearch,helpers
from elasticsearch.helpers import scan
from elasticsearch_dsl import Search

es = Elasticsearch('18.205.185.89')



#############################################################################################################


list_id=helpers.scan(es,query={"query":{"match_all": {}}},scroll='1m',index="packetstormsecurity", doc_type="items")
IDs=[item_id['_id'] for item_id in list_id]
#print(IDs)
#test=es.search(index='packetstormsecurity', filter_path=['hits.hits._*'])
#print(version)

#def all_id():
#    for id in IDs:
#        res = es.get(index="packetstormsecurity", doc_type='items', id=id)
#        print(id)
#def all_id():
for item_id in IDs:
#res = es.get(index="packetstormsecurity", doc_type='items', id='466cdc1caa1df263d9309b2595cde2e4691d9047')   ####### item_id)
#version_check=[item_version[1] for item_version in res]
#print(version_check)
#all_id()


############### This is now working for version from direct stated id number IE: > id='466cdc1caa1df263d9309b2595cde2e4691d9047
    test = es.get(index="packetstormsecurity", doc_type='items', id=item_id)
#print(test["_version"])
    wow = (test["_version"], item_id)
    print(wow)



a = es.get(index="packetstormsecurity", doc_type='items', id='466cdc1caa1df263d9309b2595cde2e4691d9047')
print(a)




#        for version in res:
#            if "'_version': 1" in version:
#               print('holly molly')
#        print(res)

#    for answer in res:
#        print(answer)


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
