from django.db import models
from django.db.models import Q
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

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

    @property
    def formatted_markdown(self): # <-- This is used in views
        return markdownify(self.content)

    def __unicode__(self):
        return self.title


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def pub_number(self):
        return Post.objects.filter(published_date__lte=self.published_date).count()

    def journal_pub_number(self):
        return Post.objects.filter(Q(published_date__lte=self.published_date)
                                   & Q(type='journal')).count()

    def blog_pub_number(self):
        return Post.objects.filter(Q(published_date__lte=self.published_date)
                                   & Q(type='blog')).count()

    def get_next_journ(self):
        # current_journ = Post.objects.get(self)
        next_journ = Post.objects.filter(Q(type='journal') & Q(published_date__gt=self.published_date)).order_by('published_date').first()
        if next_journ:
            return next_journ
        return False

    def get_next(self):
        next = Post.get_next_by_Post.objects.filter(type='journal')
        if next:
            return next.first()
        return False

    def get_prev(self):
        prev = Post.get_previous_by_published_date()
        if prev:
            return prev.first()
        return False


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=40)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def __str__(self):
        return self.author + ' - ' + self.content[:60] + '...'

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
