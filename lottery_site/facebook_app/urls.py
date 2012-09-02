from django.conf.urls import patterns, include, url
from facebook_app.views import FacebookStartPage, FacebookPagePage

urlpatterns = patterns('',

     url(r'^$', FacebookStartPage.as_view(), name='facebook_home'),
     url(r'^page/$', FacebookPagePage.as_view(), name='facebook_page'),
    
)
