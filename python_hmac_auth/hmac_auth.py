import base64
import datetime
import dateutil.tz
import hmac
from hashlib import sha256
from requests.auth import AuthBase
from urlparse import parse_qs, urlsplit, urlunsplit
from urllib import urlencode


class HmacAuth(AuthBase):
    API_KEY_QUERY_PARAM = 'apiKey'
    SIGNATURE_HTTP_HEADER = 'X-Auth-Signature'
    TIMESTAMP_HTTP_HEADER = 'X-Auth-Timestamp'
    VERSION_HTTP_HEADER = 'X-Auth-Version'
    SIGNATURE_DELIM = '\n'
    VERSION_1 = '1'

    def __init__(self, api_key, secret_key,
                 api_key_query_param = API_KEY_QUERY_PARAM,
                 signature_http_header = SIGNATURE_HTTP_HEADER,
                 timestamp_http_header = TIMESTAMP_HTTP_HEADER,
                 version_http_header = VERSION_HTTP_HEADER):
        self.api_key = api_key
        self.secret_key = secret_key
        self.api_key_query_param = api_key_query_param
        self.signature_http_header = signature_http_header
        self.timestamp_http_header = timestamp_http_header
        self.version_http_header = version_http_header

    def __call__(self, request):
        self._encode(request)
        return request

    def _encode(self, request):
        timestamp = self._get_current_timestamp()
        self._add_api_key(request)
        self._add_timestamp(request, timestamp)
        self._add_signature(request, timestamp)
        self._add_version(request, HmacAuth.VERSION_1)

    def _get_current_timestamp(self):
        # Return current UTC time in ISO8601 format
        return datetime.datetime.now(dateutil.tz.tzutc()).isoformat()

    def _add_api_key(self, request):
        # Add the API key as a query parameter
        url = request.url
        scheme, netloc, path, query_string, fragment = urlsplit(url)
        query_params = parse_qs(query_string)
        query_params[self.api_key_query_param] = self.api_key
        new_query_string = urlencode(query_params, doseq=True)
        new_url = urlunsplit((scheme, netloc, path, new_query_string, fragment))
        request.url = new_url

    def _add_timestamp(self, request, timestamp):
        request.headers[self.timestamp_http_header] = timestamp

    def _add_version(self, request, version):
        request.headers[self.version_http_header] = version

    def _add_signature(self, request, timestamp):
        method = request.method
        path = request.path_url
        content = request.body
        signature = self._sign(method, timestamp, path, content)
        request.headers[self.signature_http_header] = signature

    def _sign(self, method, timestamp, path, content):
        # Build the message to sign
        message = bytearray(method) +                       \
                  bytearray(HmacAuth.SIGNATURE_DELIM) +     \
                  bytearray(timestamp) +                    \
                  bytearray(HmacAuth.SIGNATURE_DELIM) +     \
                  bytearray(path)

        if content:
            message += bytearray(HmacAuth.SIGNATURE_DELIM) + bytearray(content)

        # Create the signature
        digest = hmac.new(self.secret_key, message, sha256).digest()
        return base64.urlsafe_b64encode(digest).strip()
