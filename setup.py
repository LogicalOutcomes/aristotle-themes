import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-aristotle-themes',
    version='0.0.2',
    packages=['aristotle_themes'],
    include_package_data=True,
    license='BSD Licence',
    description='',
    long_description=README,
    url='https://github.com/LogicalOutcomes/aristotle-themes',
    author='Rafael Capdevielle',
    author_email='rafael@logicaloutcomes.net',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'libsass',
        'aristotle-metadata-registry',
    ]
)
