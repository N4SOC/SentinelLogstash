FROM docker.elastic.co/logstash/logstash:7.17.3

ARG environment_name
ARG workspaceID
ARG workspaceKey
ARG syslog_forward

USER root

RUN dnf -y update

RUN logstash-plugin install microsoft-logstash-output-azure-loganalytics
RUN logstash-plugin install logstash-output-syslog

RUN rm -f /usr/share/logstash/pipeline/*
RUN rm -f /usr/share/logstash/config/*

COPY pipeline/ /usr/share/logstash/pipeline/
COPY config/ /usr/share/logstash/config/

RUN sed -i "s|<environment_name>|${environment_name}|g"  /usr/share/logstash/pipeline/sentinel.conf 
RUN sed -i "s|<workspaceID>|${workspaceID}|g"  /usr/share/logstash/pipeline/sentinel.conf 
RUN sed -i "s|<workspaceKey>|${workspaceKey}|g"  /usr/share/logstash/pipeline/sentinel.conf 

RUN sed -i "s|<syslog_forward>|${syslog_forward}|g"  /usr/share/logstash/pipeline/loginsight.conf


