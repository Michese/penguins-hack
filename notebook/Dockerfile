FROM alpine:3.16.0

RUN apk add --no-cache --update \
    python3 python3-dev py3-pip gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev \
    py3-pandas py3-scikit-learn py3-threadpoolctl \
    && pip install --no-cache --upgrade pip setuptools wheel \
    && pip install --no-cache jupyter joblib openpyxl

WORKDIR /app

EXPOSE 8888
  
CMD cp dep_vk.xlsx jupyter/dep_vk.xlsx && \
cp dep_tg.xlsx jupyter/dep_tg.xlsx && \
cp dep_user.csv jupyter/dep_user.csv && \
cp dep_ok.xlsx jupyter/dep_ok.xlsx && \
jupyter nbconvert app.ipynb --to python --output jupyter/app.py && \
    /usr/bin/python3 jupyter/app.py && \
    jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root