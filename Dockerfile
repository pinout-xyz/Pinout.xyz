FROM python:slim

ARG PUBLISH_DRAFT=''

WORKDIR /app

COPY . .

RUN apt-get update && \
	apt-get install -y make g++ && \
	rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

RUN if [ -n "${PUBLISH_DRAFT}" ]; then ./draft/publish.sh "${PUBLISH_DRAFT}"; fi

EXPOSE 8080

CMD ["sh", "-c", "make serve LANG=${PINOUT_LANG:-en}"]
