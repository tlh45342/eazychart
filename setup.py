from setuptools import setup

setup(
    name='eazychart',
    version='0.1.0',
    author='Tom Hamilton',
    author_email="",
    packages=['eazychart'],
    url='http://pypi.python.org/pypi/hcacheclient/',
    license='LICENSE.txt',
    description='An awesome package that does something',
    long_description=open('README.txt').read(),
    install_requires=[
       "requests",
       "pytest",
    ],
)