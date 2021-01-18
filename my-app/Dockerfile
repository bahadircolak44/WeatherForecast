# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm cache clear --force
RUN npm install
RUN npm install @vue/cli@3.7.0 -g
RUN npm install bootstrap bootstrap-vue vue-select vuetify vue-js-modal
RUN npm install vue-router vuex jquery axios popper.js
#RUN npm install sass-loader -D
#RUN npm install node-sass -D
#RUN npm -g i sass
#RUN npm install -D pug-plain-loader pug
#RUN npm install stylus stylus-loader@3
RUN npm install @trevoreyre/autocomplete-vue
RUN npm install -g nodemon
# start app
CMD ["nodemon", "--exec", "npm", "run", "serve"]