from distutils.core import setup

exec(open('python_hmac_auth/version.py').read())

with open('README.md') as f:
    readme = f.read()

setup(
    author='Bazaarvoice',
    name='python-hmac-auth',
    version=__version__,
    packages=['python_hmac_auth'],
    url='https://github.com/bazaarvoice/python-hmac-auth',
    description='Python client for jersey-hmac-auth (https://github.com/bazaarvoice/jersey-hmac-auth)',
    long_description=readme,
    install_requires=[
        "requests == 2.2.1"
    ],
    license='Apache 2.0',
)