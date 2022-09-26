FROM ubuntu:latest
ENV VERSION=1.2.0
RUN apt update && apt install --no-install-recommends --assume-yes \
 	python3 \
        vim \
	zip \
	unzip
	
COPY zip_job.py /tmp
ENTRYPOINT ["./InitialScript.sh"]	
