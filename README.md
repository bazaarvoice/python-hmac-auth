Welcome
=======

This is a Python SDK for the [jersey-hmac-auth](https://github.com/bazaarvoice/jersey-hmac-auth) library.
It enables you to encode outgoing API requests such that they can be authenticated by services that implement 
HMAC authentication using the jersey-hmac-auth library.

This SDK is essentially just a [custom authenticator](http://docs.python-requests.org/en/latest/user/advanced/#custom-authentication)
for the [Requests](http://docs.python-requests.org) library. To use it, just code your API requests using the
Requests library and add an `HmacAuth` authenticator to your calls (as demonstrated below).


Getting Started
===============

Install it locally. Just replace the version to the latest released version. For example:

```
pip install git+ssh://git@github.com/bazaarvoice/python-hmac-auth.git@v0.3
```

Then, in your code, construct requests as follows:

```python
import requests
from python_hmac_auth import HmacAuth

r = requests.get('http://example.com/api', auth=HmacAuth('api_key', 'secret_key'))
```


Contributing
============

Pull requests are always welcome and appreciated.

To submit new requests/issues or to see existing requests/issues, please 
visit the [Issues](https://github.com/bazaarvoice/python-hmac-auth/issues) page.