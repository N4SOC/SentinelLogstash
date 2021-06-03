FROM docker.elastic.co/logstash/logstash:7.13.1

ARG environment_name
ARG workspaceID
ARG workspaceKey

USER root

RUN rm -f /usr/share/logstash/pipeline/logstash.conf

RUN yum -y update

RUN logstash-plugin install microsoft-logstash-output-azure-loganalytics

COPY logstash.conf /usr/share/logstash/pipeline/logstash.conf

RUN sed -i "s|<workspaceID>|${workspaceID}|g"  /usr/share/logstash/pipeline/logstash.conf 
RUN sed -i "s|<environment_name>|${environment_name}|g"  /usr/share/logstash/pipeline/logstash.conf
RUN sed -i "s|<workspaceKey>|${workspaceKey}|g"  /usr/share/logstash/pipeline/logstash.conf

