FROM python:slim

ARG PUBLISH_DRAFT=''

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -e ".[serve,api]"

RUN if [ -n "${PUBLISH_DRAFT}" ]; then pinoutxyz boards publish "${PUBLISH_DRAFT}"; fi

EXPOSE 8080

CMD ["sh", "-c", "pinoutxyz serve --watch --lang ${PINOUT_LANG:-en}"]
