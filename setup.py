import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pennuser',
    version='0.2',
    packages=['pennuser'],
    include_package_data=True,
    license='BSD License',
    description="A simple Django app to use the University of Pennsylvania's CoSign auth and extend Django's base user.",
    long_description=README,
    url='https://github.com/wharton/django-penn-user/',
    author='Timothy Allen, the Wharton School',
    author_email='tallen@wharton.upenn.edu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
