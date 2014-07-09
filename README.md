# python-hmac-auth

HMAC authentication for Python client libraries.

This library makes it easy to add support for HMAC authentication in Python clients that (1) interface with an API that uses
[jersey-hmac-auth](https://github.com/bazaarvoice/jersey-hmac-auth) to implement authentication and (2) use the Python [Requests](http://docs.python-requests.org) library to make their API calls. 

It provides a custom authentictor that easily integrates with the Requests library and modifies all outgoing API requests by calculating a request signature and adding all the appropriate parameters/headers to the request.


## Getting Started

First install the package. You can either install the latest code on master (which should typically 
be fine) or install a particular released version.

To install the latest code from master:

```
pip install git+ssh://git@github.com/bazaarvoice/python-hmac-auth.git
```

Or, to install a particular released version (e.g. `v0.3`):

```
pip install git+ssh://git@github.com/bazaarvoice/python-hmac-auth.git@v0.3
```

Then, in your code, import the `HmacAuth` class and specify it on the `auth` parameter when issuing
API calls.

```python
import requests
from python_hmac_auth import HmacAuth

r = requests.get('http://example.com/api', auth=HmacAuth('your_api_key', 'your_secret_key'))
```

Note: If you have issues installing via the above `pip install` commands, you can file an issue or alternatively try
installing as follows:

```
git clone git@github.com:bazaarvoice/python-hmac-auth.git
python setup.py install
```


## Contributing

To submit a new request or issue, please visit the [Issues](https://github.com/bazaarvoice/python-hmac-auth/issues) page.

Pull requests are always welcome.
