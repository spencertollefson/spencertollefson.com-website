from django.db import models
from django.db.models import Q
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google
import re


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = MarkdownxField() # <-- This is the field I'm using for posts
    # now. But I should refer to ".formatted_markdown|safe" in templates.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=7,
                  choices=(('journal', 'journal'), ('blog', 'blog')),
                            default='journal',
                            )
    slug = models.SlugField(default=title)


    @property
    def formatted_markdown(self): # <-- This is used in views
        return markdownify(self.content)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        try:
            ping_google('/sitemap.xml')
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

    @models.permalink
    def get_absolute_url(self):
        if self.type == 'blog':
            return ('blogdetail', (),
                    {
                        'slug' :self.slug,
                    })
        elif self.type == 'journal':
            return ('journal_detail', (),
                        {
                            'slug' :self.slug,
                        })

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    def pub_number(self):
        return Post.objects.filter(published_date__lte=self.published_date).count()

    def journal_pub_number(self):
        return Post.objects.filter(Q(published_date__lte=self.published_date)
                                   & Q(type='journal')).count()

    def blog_pub_number(self):
        return Post.objects.filter(Q(published_date__lte=self.published_date)
                                   & Q(type='blog')).count()

    def get_next_journ(self):
        next_journ = Post.objects.filter(Q(type='journal') & Q(published_date__gt=self.published_date)).order_by('published_date').first()
        if next_journ:
            return next_journ
        return False

    def get_prev_journ(self):
        back_journ = Post.objects.filter(Q(type='journal') & Q(published_date__lt=self.published_date)).order_by('-published_date').first()
        if back_journ:
            return back_journ
        return False

    def get_next_blog(self):
        next_blog = Post.objects.filter(Q(type='blog') & Q(published_date__gt=self.published_date)).order_by('published_date').first()
        if next_blog:
            return next_blog
        return False

    def get_prev_blog(self):
        back_blog = Post.objects.filter(Q(type='blog') & Q(published_date__lt=self.published_date)).order_by('-published_date').first()
        if back_blog:
            return back_blog
        return False

    def return_img_rel_path(self):
        """
        Used for meta og:image
        """
        image = re.search(r'"\/static\/(.*?)"', self.formatted_markdown)
        if image == None:
            return None
        image_text = image.group(0)
        return image_text[1:-1]




