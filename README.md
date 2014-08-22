# python-hmac-auth

HMAC authentication for Python client libraries.

This library makes it easy to add support for HMAC authentication in Python clients that:

1. Interface with a REST API that uses
[jersey-hmac-auth](https://github.com/bazaarvoice/jersey-hmac-auth) to implement HMAC authentication, and 
2. Use the Python [Requests](http://docs.python-requests.org) library to make API calls. 

It works by providing a custom authenticator for the Requests library that modifies outgoing API calls to encode
the requests for HMAC authentication.

## Getting Started

To install:

```python
pip install python-hmac-auth
```

In your code, import the `HmacAuth` class and specify it on the `auth` parameter when issuing API calls:

```python
import requests
from python_hmac_auth import HmacAuth

response = requests.get('http://example.com/api', auth=HmacAuth('your_api_key', 'your_secret_key'))
```

## User Guide

See the [User Guide](https://github.com/bazaarvoice/jersey-hmac-auth/wiki) for jersey-hmac-auth for more details 
about HMAC authentication on the server and for clients libraries.

## Contributing

To get the code:

```sh
$ git clone git@github.com:bazaarvoice/python-hmac-auth.git
```

To submit a new request or issue, please visit the [Issues](https://github.com/bazaarvoice/python-hmac-auth/issues) page.

Pull requests are always welcome.
