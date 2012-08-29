from django.utils import simplejson as json
from base64 import urlsafe_b64decode
from hashlib import sha256
import  hmac
from facebook_app import keys
from lottery_site.settings import SITE_URL

def get_auth_url():
    oauth_url = "https://www.facebook.com/dialog/oauth/"
    oauth_url += "?client_id=%s" % keys.FACEBOOK_APP_ID
    oauth_url += "&redirect_uri=https://apps.facebook.com/%s/" % keys.FACEBOOK_APP_NAMESPACE
    oauth_url += "&scope=%s" % keys.FACEBOOK_APP_PERMISSIONS
    return oauth_url

def get_page_install_url():
    page_install_url = "http://www.facebook.com/dialog/pagetab"
    page_install_url += "?app_id=%s" % keys.FACEBOOK_APP_ID
    page_install_url += "&next=%s" % SITE_URL
    return page_install_url