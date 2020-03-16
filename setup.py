from setuptools import setup


def read(filename):
    with open(filename, 'r') as f:
        return f.read()


setup(
    name='python-hmac-auth',
    version='0.5',
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
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['requests', 'python-dateutil']
)
