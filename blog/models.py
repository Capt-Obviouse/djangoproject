from django.db import models
from django.utils import timezone

# Create your models here.
class Pages(models.Model):
    page_number = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{}".format(self.page_number)

    class Meta:
        verbose_name_plural = "pages"

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default="", blank=True)
    page_number = models.ForeignKey(Pages, default=None, on_delete=models.CASCADE, unique=True)
    created_at = models.DateTimeField(default=timezone.now(), blank=True)
    assignment = models.TextField()


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "posts"
