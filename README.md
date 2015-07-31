Retask
=======
email organization tool. The new way to do email.

## Quickstart
### Flask
Flask is a python web framwork. I stole some code from an old project I was working on so that I could get this app running quick!

1. Get pip. You can do that simply by running 'python get-pip.py' while in the retask directory. if that doesn't work for whatever reason, you can get pip [here](https://pip.pypa.io/en/latest/installing.html#install-pip). pip is a widely used installation tool for python dependencies and libraries like flask.
2. Please follow the instructions at [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/dev/virtualenvs/) in order to set up a virtual environment. A virtualenv is like a playground where you can install certain python libraries and other dependencies that only exist while the environment is activated.
2. Next, activate youre newly created virtualenv and [install Flask](http://flask.pocoo.org/docs/0.10/installation/). Just get the normal dev version, not the newest version.
3. Finally, navigate to the RetaskFlask directory and run 'python main.py' to start the server. If it is running you can navigate to the url that it provides (something like http://localhost:5000/). If it didn't work, you might need to follow the steps at the Flask website to install flask-mail or some other dependencies (try pip install flask-mail. Also make sure you are still within your virtual environment!)
4. Once the app is running, login with username 'admin' and password 'admin'.

### Meteor (Deprecated)
#### The meteor deprecation is old. please follow the instructions above for setting up with Flask.
first, download meteor by typing the following:
```
curl https://install.meteor.com/ | sh
```
to launch meteor, go to the project directory and then type 'meteor'. your terminal should now be serving the website at the given address (most likely http://localhost:3000/)
