FROM debian:12.9 

ARG span_interface

# Install prerequisities
RUN apt update
RUN apt install -y curl gpg gdb procps

# Add zeek repo
RUN echo 'deb http://download.opensuse.org/repositories/security:/zeek/Debian_10/ /' >> /etc/apt/sources.list.d/security:zeek.list
RUN curl -fsSL https://download.opensuse.org/repositories/security:zeek/Debian_10/Release.key | gpg --dearmor > /etc/apt/trusted.gpg.d/security_zeek.gpg
RUN apt update

# Install zeek
RUN apt install -y zeek

# Copy custom zeek config
RUN rm -f /opt/zeek/share/zeek/site/local.zeek
COPY local.zeek /opt/zeek/share/zeek/site/local.zeek
# Inject random salt
RUN sed -i "s|<salt>|`tr -dc A-Za-z0-9 </dev/urandom | head -c 20`|g" /opt/zeek/share/zeek/site/local.zeek

RUN rm -f /opt/zeek/etc/node.cfg
COPY node.cfg /opt/zeek/etc/node.cfg

# Inject correct sniffing interface
RUN sed -i "s|<span_interface>|${span_interface}|g"  /opt/zeek/etc/node.cfg

# Install JA3 package to fingerprint SSL
RUN /opt/zeek/bin/zkg install --force zeek/salesforce/ja3

# Install HASSH package to fingerprint SSH
RUN /opt/zeek/bin/zkg install --force zeek/salesforce/hassh

# Install Mitre BZAR package to identify lateral movement
RUN /opt/zeek/bin/zkg install --force zeek/mitre-attack/bzar

COPY zeekentry.sh /opt/zeek/

CMD /bin/bash /opt/zeek/zeekentry.sh
