from distutils.core import setup

from setuptools import find_packages

setup(
    name='multiquery',
    version="0.0.1",
    author='Aaron Halfaker',
    author_email='aaron.halfaker@gmail.com',
    py_modules=['multiquery'],
    url='https://github.org/halfak/multiquery',
    license=open('LICENSE').read(),
    description='Runs a single SQL query against a set of databases ' + \
                'concatenates the results together.',
    long_description=open('README.md').read(),
    install_requires=["docopt", "pymysql"],
    entry_points = {'console_scripts': ['multiquery=multiquery:main']},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering"
    ],
)
