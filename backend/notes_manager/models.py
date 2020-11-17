from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
