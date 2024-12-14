FROM node:20-alpine

WORKDIR /app/fe

COPY package.json ./

RUN npm ci

COPY . .
RUN npm i  tailwindcss@latest postcss@latest autoprefixer@latest
RUN npm run build --prod

EXPOSE 3000

#RUN npm install

USER node

CMD [ "npm", "start"]

