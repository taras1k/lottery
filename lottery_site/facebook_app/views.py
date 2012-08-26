from django.views.generic.edit import FormView
from facebook_app.forms import StartForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

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
        self.data['fb'] = fb_request_decode(request.POST.get('signed_request'), keys.FACEBOOK_APP_SECRET)
        pass

