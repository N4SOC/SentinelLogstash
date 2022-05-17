FROM docker.elastic.co/logstash/logstash:7.17.3

USER root

RUN yum -y update

RUN logstash-plugin install microsoft-logstash-output-azure-loganalytics
RUN logstash-plugin install logstash-output-syslog

RUN rm -f /usr/share/logstash/pipeline/*
RUN rm -f /usr/share/logstash/config/*

COPY pipeline/ /usr/share/logstash/pipeline/
COPY config/ /usr/share/logstash/config/

