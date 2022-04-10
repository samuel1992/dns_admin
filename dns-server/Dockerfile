FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y pdns-server pdns-backend-remote dnsutils && \
    apt-get clean

COPY pdns.conf /etc/powerdns/

EXPOSE 53/tcp
EXPOSE 53/udp
ENTRYPOINT ["/usr/sbin/pdns_server", "--daemon=no"]
