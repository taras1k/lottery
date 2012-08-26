from django.conf.urls import patterns, include, url
from facebook_app.views import FacebookStartPage

urlpatterns = patterns('',

     url(r'^$', FacebookStartPage.as_view(), name='facebook_home'),
    
)
