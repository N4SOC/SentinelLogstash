FROM debian:buster 

# Install prerequisities
RUN apt update
RUN apt install -y curl gpg

# Add zeek repo
RUN echo 'deb http://download.opensuse.org/repositories/security:/zeek/Debian_10/ /' >> /etc/apt/sources.list.d/security:zeek.list
RUN curl -fsSL https://download.opensuse.org/repositories/security:zeek/Debian_10/Release.key | gpg --dearmor > /etc/apt/trusted.gpg.d/security_zeek.gpg
RUN apt update

# Install zeek
RUN apt install -y zeek

# Copy custom zeek config
RUN rm -f /opt/zeek/share/zeek/site/local.zeek
COPY local.zeek /opt/zeek/share/zeek/site/local.zeek

RUN rm -f /opt/zeek/etc/node.cfg
COPY node.cfg /opt/zeek/etc/node.cfg

COPY zeekentry.sh /opt/zeek/

CMD /bin/bash /opt/zeek/zeekentry.sh

#CMD /opt/zeek/bin/zeek -i eth0 local