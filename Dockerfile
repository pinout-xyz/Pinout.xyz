FROM python:slim

COPY . ./

RUN apt-get update && \
	apt-get install -y make

RUN pip install -r requirements.txt

CMD ["make", "serve", "LANG=en"]
