FROM python:3.12.3-slim

ARG PUBLISH_DRAFT=''

COPY . ./

RUN apt-get update && \
	apt-get install -y make

RUN pip install -r requirements.txt

RUN test -n ${PUBLISH_DRAFT} && ./draft/publish.sh ${PUBLISH_DRAFT}

CMD ["bash", "-c", "make serve LANG=en"]