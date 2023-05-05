FROM node:16

WORKDIR /app

COPY package.json .

RUN npm install

RUN npm install --global gulp-cli

COPY . .

RUN gulp

FROM nginx

COPY --from=0 /app /usr/share/nginx/html
