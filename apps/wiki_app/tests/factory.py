import factory
from apps.wiki_app.models import SearchHistory
import os
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wikipedia_project.settings")


class SearchHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SearchHistory

    topic = "Default Topic"
    top_words = {"Topic": "apple", "Top Words": [["the", 79], ["in", 55]]}
    timestamp = timezone.now()
