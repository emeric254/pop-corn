FROM docker.io/python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN apk --no-cache add --virtual .build-dependencies build-base libffi-dev cargo \
    && pip install --no-cache -r requirements.txt \
    && apk del .build-dependencies \
    && rm -rf /root/.cargo/

COPY main.py  ./
COPY api  ./api/
COPY logique  ./logique/
COPY modeles  ./modeles/
COPY outils  ./outils/
COPY reference.env ./

RUN python -m compileall -b -q -f -j 0 ./ && find ./ -name "*.py" -type f -delete

EXPOSE 8088

CMD ["uvicorn", "main:app", "--proxy-headers", "--host=0.0.0.0", "--port=8088"]
