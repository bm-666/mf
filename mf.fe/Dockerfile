FROM node:20-alpine

WORKDIR /app/fe

COPY package.json ./

RUN npm install

COPY . .
RUN npm install  tailwindcss@latest postcss@latest autoprefixer@latest
#RUN npm run build

EXPOSE 3000

#RUN npm install

USER node

CMD [ "npm", "start"]

