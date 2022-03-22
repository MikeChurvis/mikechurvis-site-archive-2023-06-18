FROM nginx:1-alpine

RUN apt update \
  && apt install snapd \
  && snap install core \
  && snap refresh core \
  && snap install --classic certbot \
  && ln -s /snap/bin/certbot /usr/bin/certbot \

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

RUN certbot certonly --nginx