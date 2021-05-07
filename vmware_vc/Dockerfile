FROM logstash:7.12.0

ARG environment_name
ARG workspaceID
ARG workspaceKey

USER root

RUN yum -y update

RUN logstash-plugin install microsoft-logstash-output-azure-loganalytics

RUN rm -f /usr/share/logstash/pipeline/*
RUN rm -f /usr/share/logstash/config/*

COPY pipeline/ /usr/share/logstash/pipeline/
COPY config/ /usr/share/logstash/config/

RUN sed -i "s|<environment_name>|${environment_name}|g"  /usr/share/logstash/pipeline/sentinel.conf 
RUN sed -i "s|<workspaceID>|${workspaceID}|g"  /usr/share/logstash/pipeline/sentinel.conf 
RUN sed -i "s|<workspaceKey>|${workspaceKey}|g"  /usr/share/logstash/pipeline/sentinel.conf 

EXPOSE 4514/tcp

