from django.conf.urls import patterns, include, url
from facebook_app.views import FacebookStartPage, FacebookPagePage, CreateLotteryPage, LotteryCreatedPage

urlpatterns = patterns('',

     url(r'^$', FacebookStartPage.as_view(), name='facebook_home'),
     url(r'^page/$', FacebookPagePage.as_view(), name='facebook_page'),
     url(r'^page/create_lottery$', CreateLotteryPage.as_view(), name='lottery_create'),
     url(r'^lotery/created/$', LotteryCreatedPage.as_view(), name='lottert_created'),

)
