FROM alpine:3.16.0

RUN apk add --no-cache --update \
    python3 python3-dev py3-pip gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev \
    py3-pandas py3-scikit-learn py3-threadpoolctl \
    && pip install --no-cache --upgrade pip setuptools wheel flask joblib openpyxl \
    && export FLASK_APP=$FLASK_APP && export FLASK_ENV=$FLASK_ENV

WORKDIR /app

CMD ["python3", "app.py"]