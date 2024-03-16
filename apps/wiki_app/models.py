from django.db import models


class SearchHistory(models.Model):
    topic = models.CharField(max_length=100)
    top_words = models.JSONField(default=dict)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
