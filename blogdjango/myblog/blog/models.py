from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "entries"