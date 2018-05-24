from django.contrib.sitemaps import Sitemap
from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, item):
        last_post = Post.objects.filter(post=item)
        if last_post:
            return sorted(last_post)[-1].published_date
