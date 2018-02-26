=====
django-rest-framework-apikeys
=====

django-rest-framework-apikeys allows you to Authenticate your REST api with api keys on a per user basis.

Install
-----------
1. Install via pip::

    pip install django-rest-framework-apikeys

Quick start
-----------

1. Add "django-rest-framework-apikeys" to your INSTALLED_APPS settings like this::

    INSTALLED_APPS = [
        ...
        'django_rest_framework_apikeys',
    ]

2. Add the authentication class::

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            ...
            'django_rest_framework_apikeys.authentication.APIKeyAuthentication',
        )
    }

3. Run `python manage.py migrate`.

4. Add urls to urlconf::

    urlpatterns = [
        ...
        url(r'^apikeys/', include("django_rest_framework_apikeys.urls")),
    ]


5. Send a POST request to /apikeys/create/ to create API Key for user or create via admin

6. Add 'x-api-key' to header to Authenticate via api key::

    response = requests.get(
        url="http://0.0.0.0:8000/endpoint,
        headers={
            "x-api-key": "fd8b4a98c8f53035aeab410258430e2d86079c93",
        },
    )

