FROM ubuntu:latest

ENV VERSION=1.2.0

RUN echo "192.168.1.242   artifactory-tlv" >> /etc/hosts && apt update && apt install --no-install-recommends --assume-yes \
    python3 \
    vim \
    zip \
    unzip \
    curl

COPY ["zip_job.py", "InitialScript.sh", "/tmp/"] 

ENTRYPOINT ["/bin/sh", "-c", "chmod 777 /tmp/InitialScript.sh && /tmp/InitialScript.sh && sleep 387482748272847289"]
