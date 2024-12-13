FROM node:20-alpine

WORKDIR /app/fe

COPY package.json ./

RUN npm install

COPY . .

EXPOSE 3000

RUN npm install

CMD [ "npm", "run", "dev" ]

