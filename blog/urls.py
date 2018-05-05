from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('markdownx/', include('markdownx.urls')),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('resume/', views.resume, name='resume'),
    path('sitemap.xml/', views.sitemap, name='sitemap'),
]
