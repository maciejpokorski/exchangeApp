FROM node:lts-alpine

RUN yarn global add http-server

WORKDIR /app

COPY package.json ./
COPY yarn.lock ./

# install project dependencies
RUN yarn install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN yarn run build

EXPOSE 8080
CMD [ "http-server", "dist" ]
