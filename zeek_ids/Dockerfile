FROM debian:latest

USER root

RUN rm -f /opt/zeek/share/zeek/site/local.zeek

RUN rm -f /etc/suricata/suricata.yaml
COPY local.zeek /opt/zeek/share/zeek/site/local.zeek
COPY suricata.yaml /etc/suricata/suricata.yaml

