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

Tada !!! You are all equipped with multitenancy !!!

Note: migrations and management commands are not handled by this app. so please dont forget to use --database 
