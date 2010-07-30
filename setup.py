from setuptools import setup

setup(
    name = 'gpxcat',
    version = '0.1.0',
    description = 'Script to concatenate GPX tracks.',
    keywords = 'gps gps navigation tracks',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://github.com/svetlyak40wt/gpxcat/',
    install_requires = 'lxml',
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    scripts = ['gpxcat'],
)
