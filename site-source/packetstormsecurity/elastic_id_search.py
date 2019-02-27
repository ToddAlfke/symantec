from elasticsearch import Elasticsearch

es = Elasticsearch(['http://34.201.52.123:9200/'], verify_certs=True)

if not es.ping():
    raise ValueError("Connection failed")



get_id = es.search(index="packetstormsecurity", body={"query": {"match_all": {}}})
for row in get_id["hits"]["hits"]:
    item_id =  row["_id"]
    item = es.get(index="packetstormsecurity", doc_type='items', id=item_id)


    print(item)
