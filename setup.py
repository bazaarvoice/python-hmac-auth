from distutils.core import setup

exec(open('python_hmac_auth/version.py').read())

setup(
    author='Bazaarvoice',
    name='python-hmac-auth',
    version=__version__,
    packages=['python_hmac_auth'],
    url='https://github.com/bazaarvoice/python-hmac-auth',
    description='HMAC authentication for Python clients',
    long_description=open('README.md').read(),
    install_requires=[
        "requests == 2.2.1"
    ],
)