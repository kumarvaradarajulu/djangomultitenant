## Django Multitenant ##

This app can be used to implement multitenant architecture within your django project very easily.

Inorder to install the app


```
pip install djangomultitenant
```


Modify the project settings file as shown below


```
INSTALLED_APPS = [
    'djangomultitenant',
]

DATABASE_ROUTERS = [
    'djangomultitenant.Router',
]

MIDDLEWARE = [
    'djangomultitenant.Middleware',  # this has to be the first one
]
```
