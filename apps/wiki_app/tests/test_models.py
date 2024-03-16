from django.test import TestCase
from apps.wiki_app.tests.factory import SearchHistoryFactory
from apps.wiki_app.models import SearchHistory


class SearchHistoryModelTest(TestCase):
    """Test search history module"""

    def test_search_history_create(self):
        # Check proper create functionality in model
        search_data = SearchHistoryFactory.create()
        search_data_count = SearchHistory.objects.all().count()
        self.assertEqual(search_data_count, 1)

    def test_role_delete(self):
        # Check proper delete functionality in model
        search_data = SearchHistoryFactory.create()
        search_data = SearchHistory.objects.all()
        if search_data.count() > 0:
            search_data.delete()
        after_deletion_count = SearchHistory.objects.all().count()
        self.assertEqual(
            after_deletion_count, 0
        )
