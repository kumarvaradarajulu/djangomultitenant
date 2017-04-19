## Django Multitenant ##

This app can be used to multitenant architecture within your django project very easily. Inorder to use, you have add this app to the django installed apps and add the middleware and db router in the settings file


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
