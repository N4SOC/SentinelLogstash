FROM jasonish/suricata:latest

USER root

WORKDIR /suricata

COPY disable.conf /suricata/disable.conf
COPY suricata.yaml /suricata/suricata.yaml

RUN suricata-update update-sources
RUN suricata-update enable-source oisf/trafficid
RUN suricata-update enable-source ptresearch/attackdetection
RUN suricata-update enable-source sslbl/ja3-fingerprints
RUN suricata-update --disable-conf /suricata/disable.conf -o /suricata

