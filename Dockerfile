FROM nginx:alpine

WORKDIR /app

RUN apk update
RUN apk add py3-pip

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN mkdir upstreams
RUN mkdir locations

COPY . .
RUN rm -rf venv
RUN rm -rf .env
RUN rm -rf tools

COPY ./nginx.conf /etc/nginx/nginx.conf

RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]

EXPOSE 9080 9080