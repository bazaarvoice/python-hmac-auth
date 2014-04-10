Welcome
=======

This library enables HMAC authentication for Python clients that interface with API's implementing
authentication using the [jersey-hmac-auth](https://github.com/bazaarvoice/jersey-hmac-auth) library.

To use it, just code your API requests using the [Requests](http://docs.python-requests.org) library
and specify an ```HmacAuth``` instance as a 
[custom authenticator](http://docs.python-requests.org/en/latest/user/advanced/#custom-authentication) 
on the request (as demonstrated below).


Getting Started
===============

Install it locally. Just replace the version to the latest released version. For example:

```
pip install git+git://github.com/bazaarvoice/python-hmac-auth.git@v01
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


TODO 
====

Make issues for each of these:

- Add tests
- Add notes on building and releasing new versions of the library
