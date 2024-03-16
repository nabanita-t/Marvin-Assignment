from django.urls import path
from .views import GetWikiWordFrequencyAPIView, search_history

urlpatterns = [
    path('word-frequency-analysis/', GetWikiWordFrequencyAPIView.as_view(), name='word-frequency-analysis'),
    path('search-history/', search_history, name='search-history'),
]
