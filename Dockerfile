FROM ubuntu:latest

ENV VERSION=1.2.0

COPY zip_job.py/ /tmp/

#COPY InitialScript.sh ./

RUN apt update && apt install --no-install-recommends --assume-yes \
 	python3 \
        vim \
	zip \
	unzip \
	curl
	
#ENTRYPOINT ["./InitialScript.sh"]	
