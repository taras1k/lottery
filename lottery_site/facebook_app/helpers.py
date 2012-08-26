from django.utils import simplejson as json
import base64, hmac, hashlib
from facebook_app import keys

def fb_request_decode(signed_request):
    s = [s.encode('ascii') for s in signed_request.split('.')]

    fb_sig = base64.urlsafe_b64decode(s[0] + '=')
    fb_data = json.loads(base64.urlsafe_b64decode(s[1]))
    fb_hash = hmac.new(keys.FACEBOOK_APP_SECRET, s[1], hashlib.sha256).digest()

    sig_match = False
    if fb_sig == fb_hash:
        sig_match = True

    auth = False
    if 'user_id' in fb_data:
        auth = True

    return {
        'fb_sig' : fb_sig,
        'fb_data' : fb_data,
        'fb_hash' : fb_hash,
        'sig_match' : sig_match,
        'auth' : auth,
    }


def get_auth_url():
    oauth_url = "https://www.facebook.com/dialog/oauth/"
    oauth_url += "?client_id=%s" % keys.FACEBOOK_APP_ID
    oauth_url += "&redirect_uri=https://apps.facebook.com/%s/" % keys.FACEBOOK_APP_NAMESPACE
    oauth_url += "&scope=%s" % keys.FACEBOOK_APP_PERMISSIONS
    return oauth_url