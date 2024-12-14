FROM node:20-alpine

WORKDIR /app/fe

COPY package.json ./

RUN npm install --production

COPY . .
RUN npm run build

EXPOSE 3000

#RUN npm install

USER node

CMD [ "npm", "start"]

