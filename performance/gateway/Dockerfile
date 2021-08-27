FROM node:14-alpine

COPY package.json gateway.js ./
RUN npm install

USER node
CMD node gateway.js