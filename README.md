# CharlottesWeb Scrapy Spider

This is a Python Scrapy Elasticsearch project that scrapes unstructured data from web sources and pushes it into Elasticsearch as structured objects. Projects are located in directory site-source, and are dynamically run. Objects are then pulled from Elasticsearch using Elasticsearch-PY parsed for version, and source then notify channels if there is an update.


## Docker
### TO BUILD:

 `docker build -t charlottesweb .`

### TO RUN:
If the repo is pulled down from Git and injected into container with no persistent volume store

 `docker run -d charlottesweb`

To run with persistent volume store

 `docker volume create --name vol`

 `docker run -d -v vol:/data charlottesweb `

Dockerfile
```
FROM ubuntu:latest
VOLUME /data
```

## CharlottesWeb runtime
Running the container an ENTRYPOINT module charlottesweb.py initializes the Scrapy spider scrape by running 'scrapy crawl charlotte' in all projects starting a subprocess for each spider. It then runs the update.py module to test for version, and notify channels for version 1 "new Item ID added".

### Scrapy Environment Prerequisites
1. Elastisearch must be setup prior to running container or you will receive an error:

``Connection to Elasticsearch failed. Update Elasticsearch configuration and try again.``

  You must have a running instance of Elastisearch with access to port 9200 for API and update the ElasticsearchConfig.py module with the IP address for your node or cluster. There is a provided ELK Docker stack within the docker directory of this repo.

2. After the first run of charlottesweb an index, type, and objects will populate Elastisearch. Kibana may be used for creating an index pattern to view your imported data.

3. The update.py module is responsible for checking the version of the objects stored and providing a notification to the proper channel. **"IE: Slack, Email"**

Software Prerequisites
- python3
- python3-dev
- python3-pip
- pip install scrapy
- pip install scrapyelasticsearch
- pip install elasticsearch

To learn more about Scrapy you may visit https://docs.scrapy.org/en/latest/
