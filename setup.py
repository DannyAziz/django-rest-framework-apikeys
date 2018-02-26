import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_rest_framework_apikeys',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='django-rest-framework-apikeys allows you to Authenticate your REST api with api keys on a per user basis.',
    long_description=README,
    url='https://github.com/DannyAziz/django-rest-framework-apikeys',
    download_url='https://github.com/DannyAziz/django-rest-framework-apikeys/archive/0.1.tar.gz',
    author='DannyAziz',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)