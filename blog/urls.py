from django.urls import include, path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.about, name='about'),
    path('blog/', views.post_list, name='post_list'),
    path('journal/', views.journal_list, name='journal_list'),
    path('markdownx/', include('markdownx.urls')),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('journal/<int:pk>/', views.journal_detail, name='journal_detail'),
    path('resume/', views.resume, name='resume'),
    path('sitemap.xml/', views.sitemap, name='sitemap'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # path('drafts/', views.post_draft_list, name='post_draft_list'),
]
