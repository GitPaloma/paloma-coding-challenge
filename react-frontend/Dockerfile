FROM node:16-alpine

WORKDIR /usr/src/react

COPY package.json .
COPY package-lock.json .
RUN npm ci

COPY . .
