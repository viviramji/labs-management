
# Laboratories Manager

** SOME CODE WAS TAKEN FROM THE TUTORIAL [Flaskr](http://flask.pocoo.org/docs/1.0/tutorial/) AND ADAPTED TO OUR PROJECT. **

For running this app, feel free to follow the next steps.

First, clone this repo
```  
$ git clone https://github.com/viviramji/labs-management.git
```
After that, we I have a new directory named ` labs-management `, move to it.

```  
$ cd labs-management
```
Let's set up our virutal environment, if you're using Python 3.x you do not have to install a virutal environment module, otherwise follow this link to the official documentation [Here](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments).

On windows
```
$ py -3 -m venv my-venv
```

Now you can see a new folder called my-venv, ` my-venv ` correspond  to your virutal environment .

Activate your virtual environment  using
```
$ my-venv\Scripts\activate
```
Now your promt looks like this
```
( my-venv ) $ 
```
Now, lets set our environment  variable 
```
( my-venv ) $ set FLASK_APP=study_room
( my-venv ) $ set FLASK_DEV=development
( my-venv ) $ set FLASK_DEBUG=1
( my-venv ) $ flask init-db
Initialized the database.
```
Now we have all, just run ` flask run ` command
```
( my-venv ) $ flask run
 * Serving Flask app "study_room" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 785-815-349
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now, go to your browser and register or login an user.

*Note: it's important to clarify that your ` database ` is going to be empty, and any labs will be shown. 
To solve this add a lab or a admin user using ` SQLiteStudio `*

Thanks, any suggestion is welcome.
