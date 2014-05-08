Welcome
=======

This is a Python SDK for the [jersey-hmac-auth](https://github.com/bazaarvoice/jersey-hmac-auth) library.
It enables you to encode outgoing API requests such that they can be authenticated by services that implement 
HMAC authentication using the jersey-hmac-auth library.

This SDK is essentially just a 
[custom authenticator](http://docs.python-requests.org/en/latest/user/advanced/#custom-authentication) for the 
[Requests](http://docs.python-requests.org) library. To use it, just code your API requests using the
Requests library and add an `HmacAuth` authenticator to your calls (as demonstrated below).


Getting Started
===============

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


Contributing
============

Pull requests are always welcome and appreciated.

To submit new requests/issues or to see existing requests/issues, please 
visit the [Issues](https://github.com/bazaarvoice/python-hmac-auth/issues) page.
