FROM nginx:alpine-perl

WORKDIR /app

RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
RUN apk update
RUN apk add nginx@edge nginx-mod-http-geoip@edge

RUN apk add --no-cache nginx-mod-http-perl

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./upstreams /app/upstreams
COPY ./locations /app/locations

CMD ["nginx", "-g", "daemon off;"]

EXPOSE 9080 9080