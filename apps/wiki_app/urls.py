from django.urls import path
from .views import GetWikiWordFrequencyAPIView, GetSearchHistoryAPIView

app_name = "wiki"

urlpatterns = [
    path('word-frequency-analysis/', GetWikiWordFrequencyAPIView.as_view(), name='word-frequency-analysis'),
    path('search-history/', GetSearchHistoryAPIView.as_view(), name='search-history'),
]
