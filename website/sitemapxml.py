from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Post.objects.filter(type='blog')

    def lastmod(self, item):
        last_post = Post.objects.filter(title=item)
        if last_post:
            return sorted(last_post)[-1].published_date

class JournalSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Post.objects.filter(type='journal')

    def lastmod(self, item):
        last_post = Post.objects.filter(title=item)
        if last_post:
            return sorted(last_post)[-1].published_date


class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['about', 'bloglist', 'journal_list', 'resume',]

    def location(self, item):
        return reverse(item)