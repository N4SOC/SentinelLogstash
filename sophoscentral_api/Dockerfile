FROM debian:12.10 

ARG sophosAPIToken
ARG sophosAPIid
ARG sophosAPIsecret
ARG sophosAPItenant

USER root

RUN apt update
RUN apt install -y git python3

WORKDIR /usr/share/sophos_siem
RUN git clone https://github.com/sophos/Sophos-Central-SIEM-Integration.git .
RUN rm config.ini
COPY config.ini /usr/share/sophos_siem/
RUN sed -i "s|<sophosAPIToken>|${sophosAPIToken}|g"  /usr/share/sophos_siem/config.ini
RUN sed -i "s|<sophosAPIid>|${sophosAPIid}|g"  /usr/share/sophos_siem/config.ini
RUN sed -i "s|<sophosAPIsecret>|${sophosAPIsecret}|g"  /usr/share/sophos_siem/config.ini
RUN sed -i "s|<sophosAPItenant>|${sophosAPItenant}|g"  /usr/share/sophos_siem/config.ini

COPY sophosentry.sh /usr/share/sophos_siem/
ENTRYPOINT ["/bin/bash", "sophosentry.sh" ]

# CMD [ "/bin/bash" ]

