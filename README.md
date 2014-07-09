# python-hmac-auth

Python-based HMAC authentication for client libraries that use 
[jersey-hmac-auth](https://github.com/bazaarvoice/jersey-hmac-auth) to implement API authentication.

This library makes it easy to add support for HMAC authentication in Python clients that use the Python 
[Requests](http://docs.python-requests.org) library. It modifies all outgoing API requests to include the appropriate 
parameters/headers so that they can be authenticated by the server. It does this by providing a
[custom authenticator](http://docs.python-requests.org/en/latest/user/advanced/#custom-authentication) that modifies  requests that you make using the Requests library.


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
