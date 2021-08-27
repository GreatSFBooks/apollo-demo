FROM node:14-alpine

COPY package.json server.js schema.graphql data.json ./
RUN npm install

USER node
CMD node server.js