from django.conf.urls import patterns, include, url
from facebook_app.views import FacebookStartPage, FacebookPagePage, CreateLotteryPage, LotteryCreatedPage

urlpatterns = patterns('',

     url(r'^$', FacebookStartPage.as_view(), name='facebok_app.facebook_home'),
     url(r'^page/$', FacebookPagePage.as_view(), name='facebook_app.facebook_page'),
     url(r'^page/create_lottery$', CreateLotteryPage.as_view(), name='facebook_app.create_lottery'),
     url(r'^lotery/created/$', LotteryCreatedPage.as_view(), name='facebook_app.lottery_created'),

)
