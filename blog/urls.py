from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from . import views
from website.sitemapxml import BlogSitemap, JournalSitemap, StaticSitemap

sitemaps = {'static': StaticSitemap, 'dynamic': BlogSitemap, 'dynamic': JournalSitemap,}



urlpatterns = [
    path('', views.about, name='about'),
    path('blog/', views.bloglist, name='bloglist'),
    path('blog/<slug:slug>/', views.blogdetail, name='blogdetail'),
    path('journal/', views.journal_list, name='journal_list'),
    path('markdownx/', include('markdownx.urls')),
    path('journal/<slug:slug>/', views.journal_detail, name='journal_detail'),
    path('resume/', views.resume, name='resume'),

    # SEO
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    #Robots
    path('robots.txt', views.robots, name='robots'),

    # path('drafts/', views.post_draft_list, name='post_draft_list'),
    # re_path(r'^blog/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail')
]
