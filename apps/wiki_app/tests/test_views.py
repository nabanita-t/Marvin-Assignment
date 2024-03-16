import json
from django.urls import reverse
from rest_framework import status
from apps.wiki_app.models import SearchHistory
from rest_framework.test import APITestCase
import random
from apps.wiki_app.tests.factory import SearchHistoryFactory


class WikiWordSearchTest(APITestCase):

    def test_wiki_word_search_fail(self):
        """Wikipedia word search fail test"""

        url = reverse("wiki:word-frequency-analysis") + "?topic=lily"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wiki_word_search_success(self):
        """Wikipedia word search success test"""

        url = reverse("wiki:word-frequency-analysis") + "?topic=towel&n=10"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_wiki_search_history_table_success(self):
        """Wikipedia word search success and search history table populate test"""

        url = reverse("wiki:word-frequency-analysis") + "?topic=apple&n=10"
        response = self.client.get(url)
        search_history = SearchHistory.objects.all().count()
        self.assertEquals(search_history, 1)

    def test_wiki_search_history_table_check(self):
        """Wikipedia word search success / fail and search history table populate check test"""
        word_list = ["apple", "banana", "orange", "grape", "kiwi"]
        random_topic = random.choice(word_list)
        url = reverse("wiki:word-frequency-analysis") + "?topic=" + random_topic + "&n=10"
        response = self.client.get(url)
        search_history = SearchHistory.objects.all().count()
        if response.status_code == 400:
            self.assertEquals(search_history, 0)
        else:
            self.assertEquals(search_history, 1)

    def test_search_history_empty_list(self):
        """Search History Empty response check"""

        url = reverse("wiki:search-history")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 0)

    def test_search_history_success(self):
        """Search History Non-Empty response check"""
        SearchHistoryFactory.create()
        url = reverse("wiki:search-history")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)
