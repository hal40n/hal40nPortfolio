FROM node:20.5.1-alpine

RUN apk add --no-cache git bash

WORKDIR /app/frontend
COPY  . .

RUN apk update

RUN npm install -g npm@10.8.1

CMD [ "npm", "run", "dev", "--host" ]