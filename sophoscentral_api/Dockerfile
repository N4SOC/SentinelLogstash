FROM debian:buster 

ARG sophosAPIToken
ARG sophosAPIToken
ARG sophosAPIid
ARG sophosAPIsecret

USER root

RUN apt update
RUN apt install -y git python3

WORKDIR /usr/share/sophos_siem
RUN git clone https://github.com/sophos/Sophos-Central-SIEM-Integration.git .
RUN rm config.ini
COPY config.ini /usr/share/sophos_siem/
RUN sed -i "s|<sophosAPIToken>|${sophosAPIToken}|g"  /usr/share/sophos_siem/config.ini

COPY sophosentry.sh /usr/share/sophos_siem/
ENTRYPOINT ["/bin/bash", "sophosentry.sh" ]

# CMD [ "/bin/bash" ]

