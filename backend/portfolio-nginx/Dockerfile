FROM nginx:1-alpine

RUN apk add certbot certbot-nginx \
  && rm /etc/nginx/conf.d/default.conf \
  && mkdir /etc/letsencrypt \
  && mkdir -p /var/www/portfolio/
  
COPY nginx.conf /etc/nginx/conf.d
