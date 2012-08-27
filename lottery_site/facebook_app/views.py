from django.views.generic.edit import FormView
from facebook_app.forms import StartForm
from facebook_app.helpers import get_auth_url
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from facepy import GraphAPI, SignedRequest
from keys import FACEBOOK_APP_SECRET


class FacebookStartPage(FormView):

    form_class = StartForm
    template_name = 'facebook_app/index.html'

    def __init__(self, *args, **kwargs):
        self.data = {}

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(FacebookStartPage, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FacebookStartPage, self).get_context_data(**kwargs)
        context['fb_user'] = self.data.get('fb_user', 'empty')
        return context

    def post(self, request, *args, **kwargs):
        signed_request = request.POST.get('signed_request')
        signed_request = SignedRequest(signed_request, FACEBOOK_APP_SECRET)
        if signed_request.oauth_token is None:            
            self.data['oauth_url'] = get_auth_url()
        else:
            oauth_token = signed_request.oauth_token.token
            graph = GraphAPI(oauth_token)
            self.data['fb']['user'] = graph.get('me')
        return self.render_to_response(self.data)

