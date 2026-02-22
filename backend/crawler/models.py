from django.db import models

class Keyword(models.Model):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word

class WebPage(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    pagerank_score = models.FloatField(default=0.0)
    last_crawled = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else self.url

class Link(models.Model):
    from_page = models.ForeignKey(WebPage, related_name='outgoing_links', on_delete=models.CASCADE)
    to_page = models.ForeignKey(WebPage, related_name='incoming_links', on_delete=models.CASCADE)

    class Meta:
        # Combined primary key, so that one link
        # cannot be counted twice
        unique_together = ('from_page', 'to_page')

class PageKeyword(models.Model):
    page = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    # Occurences
    frequency = models.IntegerField(default=1)

    class Meta:
        unique_together = ('page', 'keyword')