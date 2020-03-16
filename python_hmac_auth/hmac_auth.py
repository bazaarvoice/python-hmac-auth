import base64
import datetime
import dateutil.tz
import hmac
from hashlib import sha256
from requests.auth import AuthBase

try:
    from urlparse import parse_qs, urlsplit, urlunsplit
    from urllib import urlencode
except:
    from urllib.parse import parse_qs, urlsplit, urlunsplit, urlencode


def _get_current_timestamp():
    # Return current UTC time in ISO8601 format
    return datetime.datetime.now(dateutil.tz.tzutc()).isoformat()


class HmacAuth(AuthBase):
    API_KEY_QUERY_PARAM = 'apiKey'
    SIGNATURE_HTTP_HEADER = 'X-Auth-Signature'
    TIMESTAMP_HTTP_HEADER = 'X-Auth-Timestamp'
    VERSION_HTTP_HEADER = 'X-Auth-Version'
    SIGNATURE_DELIM = '\n'
    VERSION_1 = '1'

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        self._encode(request)
        return request

    def _encode(self, request):
        timestamp = _get_current_timestamp()
        self._add_api_key(request)
        self._add_signature(request, timestamp)
        request.headers[HmacAuth.TIMESTAMP_HTTP_HEADER] = timestamp
        request.headers[HmacAuth.VERSION_HTTP_HEADER] = HmacAuth.VERSION_1

    def _add_api_key(self, request):
        # Add the API key as a query parameter
        url = request.url
        scheme, netloc, path, query_string, fragment = urlsplit(url)
        query_params = parse_qs(query_string)
        query_params[HmacAuth.API_KEY_QUERY_PARAM] = self.api_key
        new_query_string = urlencode(query_params, doseq=True)
        new_url = urlunsplit((scheme, netloc, path, new_query_string, fragment))
        request.url = new_url

    def _add_signature(self, request, timestamp):
        method = request.method
        path = request.path_url
        content = request.body
        signature = self._sign(method, timestamp, path, content)
        request.headers[HmacAuth.SIGNATURE_HTTP_HEADER] = signature

    def _sign(self, method, timestamp, path, content):
        # Build the message to sign

        message = bytearray(method, 'utf-8') + \
                  bytearray(HmacAuth.SIGNATURE_DELIM, 'utf-8') + \
                  bytearray(timestamp, 'utf-8') + \
                  bytearray(HmacAuth.SIGNATURE_DELIM, 'utf-8') + \
                  bytearray(path, 'utf-8')

        if content:
            message += bytearray(HmacAuth.SIGNATURE_DELIM, 'utf-8') + bytearray(content, 'utf-8')

        # Create the signature
        digest = hmac.new(key=bytearray(self.secret_key, 'utf-8'), msg=message, digestmod=sha256).digest()
        return base64.urlsafe_b64encode(digest).strip()
