FROM node:16 AS build

WORKDIR /app

COPY package.json .

RUN yarn

COPY . .

RUN yarn build

FROM nginx

COPY --from=build /app/build /usr/share/nginx/html

#ENTRYPOINT ["nginx", "-g", "daemon off;"]



