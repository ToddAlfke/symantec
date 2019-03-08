#### This is a Python Scrapy Spider ####
FROM ubuntu:latest

ENV ENVIRONMENT=/home/ubuntu
#ENV ENVIRONMENT=/volume

RUN apt-get update -y && \
    apt-get install python3 -y && \
    apt-get install python3-dev -y && \
    apt-get install python3-pip -y && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    pip install scrapy && \
    pip install scrapyelasticsearch && \
    pip install elasticsearch

#RUN apt-get install -y git && \
#git clone -b master https://<token>:x-oauth-basic@https://github.com/ToddAlfke/symantec.git $ENVIRONMENT
#or
COPY . $ENVIRONMENT

RUN ln -s $ENVIRONMENT env && \
    cp -r env /etc/environment

WORKDIR $ENVIRONMENT


#ENTRYPOINT ["python", "charlottesweb.py"]
