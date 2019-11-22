from setuptools import setup

def read(filename):
    return open(filename).read()

setup(
    name='python-hmac-auth',
    version='1.0',
    description='Python client for jersey-hmac-auth (https://github.com/bazaarvoice/jersey-hmac-auth)',
    long_description=read('README.md'),
    url='https://github.com/bazaarvoice/python-hmac-auth',
    license=read('LICENSE'),
    author='Bazaarvoice',
    author_email='benton.porter@bazaarvoice.com',
    packages=['python_hmac_auth'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    install_requires=['requests', 'python-dateutil']
)