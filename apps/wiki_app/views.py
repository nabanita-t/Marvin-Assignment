from rest_framework import status, generics, parsers, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SearchHistory
from .serializers import SearchHistorySerializer
from .constants import ApplicationMessages
import wikipedia


class GetWikiWordFrequencyAPIView(generics.GenericAPIView):
    """Get wikipedia word frequency API View -- It takes two parameters from users in the param i.e topic and
    n = number of top word frequency, and renders the output of top n frequently used words in that
    wikipedia search result with number of occurrences. This APi also stores the search history
    in a model named Search History"""

    parser_classes = (parsers.JSONParser,)
    filter_backends = (
        # keyword search
        filters.SearchFilter,
    )
    search_fields = [
        "title",
    ]

    def get_queryset(self, topic=None):
        """Get the data from wikipedia depending on the given topic"""
        return wikipedia.page(topic)

    def get(self, request, *args, **kwargs):
        """Derive the word frequency depending on the provided topic and n = number of top results"""
        topic = request.query_params.get('topic', None)
        n = int(request.query_params.get('n', 10))  # Default to top 10 words if n is not provided

        if not topic:
            return Response(ApplicationMessages.TOPIC_N_FOUND, status=status.HTTP_400_BAD_REQUEST)
        try:
            page = self.get_queryset(topic)
            text = page.content
            words = text.split()
            word_freq = {}
            for word in words:
                # Check if word is alphabets or not (it should not count special characters)
                if word.isalpha():
                    word = word.lower()  # Convert to lowercase to avoid duplicate word counts
                    word_freq[word] = word_freq.get(word, 0) + 1
            # Sorting the words w.r.t frequency
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            # Slicing the top n words from the array of sorted word frequency wise
            top_n_words = sorted_words[:n]
            result_data = {'Topic': topic, 'Top Words': top_n_words}
            data = {
                "topic": topic,
                "top_words": result_data
            }
            SearchHistory.objects.create(**data)
            return Response(data=result_data, status=status.HTTP_200_OK)
        except wikipedia.exceptions.PageError:
            return Response(ApplicationMessages.WIKI_PAGE_N_FOUND, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(ApplicationMessages.RESULT_N_MATCH, status=status.HTTP_400_BAD_REQUEST)


class GetSearchHistoryAPIView(generics.GenericAPIView):
    """Get wikipedia search history API View . It renders all the search history stored in the Database from
    the Wikipedia Search API success response. The default ordering in this API is with respect to latest timestamp """

    parser_classes = (parsers.JSONParser,)
    filter_backends = (
        # keyword search
        filters.SearchFilter,
    )
    search_fields = [
        "title",
    ]
    # pagination_class = pagination.LargePagination
    serializer_class = SearchHistorySerializer

    def get_queryset(self):
        """Get all data from search history table w.r.t timestamp (latest first)"""
        return SearchHistory.objects.all().order_by("-timestamp")

    def get(self, request, *args, **kwargs):
        """Get Search History Data from Search history table"""
        try:
            filtered_queryset = self.filter_queryset(queryset=self.get_queryset())
            serializers = self.serializer_class(filtered_queryset, many=True)
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
