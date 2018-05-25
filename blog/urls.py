from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from . import views
from website.sitemapxml import BlogSitemap, StaticSitemap

sitemaps = {'static': StaticSitemap, 'dynamic': BlogSitemap}



urlpatterns = [
    path('', views.about, name='about'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('journal/', views.journal_list, name='journal_list'),
    path('markdownx/', include('markdownx.urls')),
    path('journal/<int:pk>/', views.journal_detail, name='journal_detail'),
    path('resume/', views.resume, name='resume'),

    # SEO
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),


    # path('drafts/', views.post_draft_list, name='post_draft_list'),
    # re_path(r'^blog/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail')
]
