from django.views.generic import FormView
from facebook_app.forms import StartForm

class FacebookStartPage(FormView):

	form_class = StartForm
	template_name = 'facebook_app/index.html'
