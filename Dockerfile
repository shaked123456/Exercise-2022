FROM ubuntu:latest

ENV VERSION=1.2.0

COPY conf/ /opt/docker/

RUN apt update && apt install --no-install-recommends --assume-yes \
 	python3 \
        vim \
	zip \
	unzip
	
ENTRYPOINT ["./InitialScript.sh"]	
