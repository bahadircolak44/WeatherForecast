# WeatherForecast
weather forecast application
You can run it in two ways:
-    # Docker
    $ docker-compose up
    
 - If you want to use docker, you should change database settings in settings.py.
    Use postgresql, command out sqlite.
 - Nginx has been implemented, need to be command out from docker-compose.yaml
 
    
or  

-    # MacOS, Linux
    $ python -m venv venv
    $ source venv/bin/activate
    
-    # Windows
    $ py -m venv venv
    $ .\venv\Scripts\activate
    
-    # Library Installation
    $ pip install -r requirements.txt
    $ cd my-app
    $ npm install
    $ npm install i @vue/cli@3.7.0
    $ npm install i bootstrap bootstrap-vue vue-select vuetify vue-js-modal vue-router vuex jquery axios popper.js @trevoreyre/autocomplete-vue
    
-    # RUN VUE
    $ cd my-app
    $ npm run serve
    
   - If you have trouble while running vue server, delete my-app/package-lock.json and run npm install again

-    # RUN DJANGO
    $ python manage.py runserver