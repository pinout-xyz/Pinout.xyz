FROM python:2.7-slim

COPY . ./

RUN apt-get update && \
	apt-get install -y make

RUN pip install -r requirements.txt

CMD ["bash", "-c", "make serve LANG=en"]