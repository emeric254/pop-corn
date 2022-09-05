####
# Stage 0 - build
####

FROM docker.io/node:lts as node

WORKDIR /app

COPY package.json package-lock.json  ./

RUN npm config set fund false
RUN npm install

COPY vite.config.js index.html  ./
COPY public  ./public/
COPY src  ./src/

RUN rm ./public/donnees

RUN npm run build


####
# Stage 1 - final image
####

FROM docker.io/alpine:latest

RUN apk --no-cache add nginx brotli nginx-mod-http-brotli

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=node /app/dist/ /usr/share/nginx/html/

# following lines are taken from https://github.com/nginxinc/docker-nginx/blob/master/Dockerfile-alpine.template

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 8080

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]
