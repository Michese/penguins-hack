FROM alpine:3.16.0

RUN apk update
RUN apk add --no-cache --update nodejs npm
RUN npm install -g @vue/cli
WORKDIR /var/www/html

EXPOSE 8080

CMD npm i ; npm run serve
