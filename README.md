# symantec
Symantec Project

This is a Python Scrapy Elasticsearch project that scrapes unstructured data from web sources and pushes it into Elasticsearch as structured objects. Projects are located in directory site-source, and are dynamically run. Objects are then pulled from Elasticsearch using Elasticsearch-PY and parsed for version, then notify channels if there is an update.

The module charlottesweb.py first performs the Scrapy spider scrape by running 'scrapy crawl charlotte' in all projects starting a subprocess for each spider. It then runs the notifications update.py module to test for version, and notify channels for version 1 "latest update".

TO BUILD:
 " docker build -t charlottesweb . "

TO RUN:
 " docker run -d charlottesweb "


#### IN TEST: A volume may be setup and used to store the contents of the Symantec Repo for the COPY command
#### The intention is that projects stored in site-source directory can be updated or new projects
#### added without affecting the runtime of the container. If a volume is used the COPY & WORKDIR
#### within the Dockerfile must be changed to reflect the volume name.
#### If a volume is used there will also be the need for updating modules charlottesweb.py, Scrapy modules
#### in site-source, and notifications to reflect the updated path.
