import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-monaco-editor',
    version='3.0',
    packages=['djangomonacoeditor'],
    description='Monaco editor widget in the Django Admin',
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
    author='Collin Walker',
    author_email='collin+github@solublecode.dev',
    url='https://github.com/solublecode/django-monaco-editor',
    keywords=['django', 'monaco'],
    platforms=['OS Independent'],
    license='MIT',
    install_requires=[
        'Django>=2.0',
    ]
)
