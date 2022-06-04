FROM nginx:1-alpine

RUN apk add certbot certbot-nginx \
  && rm -f /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/nginx.conf \
  && mkdir /etc/letsencrypt \
  && mkdir -p /var/www/html/ \
  && mkdir -p /var/www/letsencrypt

COPY nginx.conf /etc/nginx/conf.d