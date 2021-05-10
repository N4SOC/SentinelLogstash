FROM jasonish/suricata:latest

USER root

RUN rm -f /etc/suricata/suricata.yaml
COPY suricata.yaml /etc/suricata/suricata.yaml

COPY disable.conf /etc/suricata/disable.conf

RUN suricata-update update-sources
RUN suricata-update enable-source oisf/trafficid
RUN suricata-update enable-source ptresearch/attackdetection
RUN suricata-update enable-source sslbl/ja3-fingerprints
RUN suricata-update

