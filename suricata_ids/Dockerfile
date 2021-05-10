FROM jasonish/suricata:latest

USER root

COPY disable.conf /tmp/disable.conf
RUN cp /tmp/disable.conf /etc/suricata/

RUN rm -f /etc/suricata/suricata.yaml
COPY suricata.yaml /etc/suricata/suricata.yaml

RUN suricata-update update-sources
RUN suricata-update enable-source oisf/trafficid
RUN suricata-update enable-source ptresearch/attackdetection
RUN suricata-update enable-source sslbl/ja3-fingerprints
RUN suricata-update

