FROM logstash:7.12.0

ARG workspaceId
ARG workspaceKey

USER root

RUN rm -f /usr/share/logstash/pipeline/logstash.conf

RUN yum -y update
RUN logstash-plugin install logstash-codec-netflow
RUN logstash-plugin install microsoft-logstash-output-azure-loganalytics

COPY logstash.conf /usr/share/logstash/pipeline/logstash.conf
RUN sed -i "s/<workspaceID>/${workspaceID}/g"  /usr/share/logstash/pipeline/logstash.conf
RUN sed -i "s/<workspaceKey>/${workspaceKey}}/g"  /usr/share/logstash/pipeline/logstash.conf

EXPOSE 2514/tcp

