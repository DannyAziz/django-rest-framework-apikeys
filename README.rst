=====
drf_apikeys
=====

drf-apikeys allows you to Authenticate your REST api with api keys on a per user basis.

Quick start
-----------

1. Add "drf_apikeys" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'drf_apikeys',
    ]

2. Add the authenticated class::

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            ...
            'drf_apikeys.authentication.APIKeyAuthentication',
        )
    }

3. Run `python manage.py migrate`.

4. Add urls to urlconf::

    urlpatterns = [
        ...
        url(r'^apikeys/', include("drf_apikeys.urls")),
    ]


5. go to /apikeys/create/ and create Api key for user

6. Add 'x-api-key' to header to Authenticate via api key.