from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from . import views

tsa_claim


urlpatterns = [
    path('', views.about, name='about'),
    path('blog/', views.bloglist, name='bloglist'),
    path('blog/<slug:slug>/', views.blogdetail, name='blogdetail'),
    path('journal/', views.journal_list, name='journal_list'),
    path('markdownx/', include('markdownx.urls')),
    path('journal/<slug:slug>/', views.journal_detail, name='journal_detail'),
    path('resume/', views.resume, name='resume'),
    path('tsa-claim-outcome-prediction/', views.tsa_claim, name='tsa_claim'),
    path('do_prediction_multiple_days/', csrf_exempt(views.do_prediction_multiple_days), name='do_prediction_multiple_days'),



    #Robots
    path('robots.txt', views.robots, name='robots'),

    # path('drafts/', views.post_draft_list, name='post_draft_list'),
    # re_path(r'^blog/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail')
]
