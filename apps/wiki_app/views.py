from rest_framework import status, generics, parsers, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SearchHistory
from .serializers import SearchHistorySerializer
from .constants import ApplicationMessages
import wikipedia


# @api_view(['GET'])
# def word_frequency_analysis(request):
#     topic = request.query_params.get('topic', None)
#     n = int(request.query_params.get('n', 10))  # Default to top 10 words if n is not provided
#
#     if not topic:
#         return Response({'error': 'Topic parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
#
#     try:
#         page = wikipedia.page(topic)
#         text = page.content
#         words = text.split()
#         word_freq = {}
#         for word in words:
#             word = word.lower()  # Convert to lowercase to avoid counting same words differently
#             word_freq[word] = word_freq.get(word, 0) + 1
#         sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
#         top_n_words = sorted_words[:n]
#         return Response({'topic': topic, 'top_words': top_n_words}, status=status.HTTP_200_OK)
#     except wikipedia.exceptions.PageError:
#         return Response({'error': 'Wikipedia page not found for the given topic'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def search_history(request):
    searches = SearchHistory.objects.all()
    serializer = SearchHistorySerializer(searches, many=True)
    return Response(serializer.data)


class GetWikiWordFrequencyAPIView(generics.GenericAPIView):
    """Get wikipedia word frequency API View"""

    parser_classes = (parsers.JSONParser,)
    filter_backends = (
        # keyword search
        filters.SearchFilter,
    )
    search_fields = [
        "title",
    ]
    # pagination_class = pagination.LargePagination

    def get_queryset(self, topic=None):
        """Get the data from wikipedia depending on the given topic"""
        return wikipedia.page(topic)

    def get(self, request, *args, **kwargs):
        """Derive the word frequency depending on the provided topic and n = number of top results"""
        topic = request.query_params.get('topic', None)
        n = int(request.query_params.get('n', 10))  # Default to top 10 words if n is not provided

        if not topic:
            return Response(ApplicationMessages.TOPIC_N_FOUND, status=status.HTTP_400_BAD_REQUEST)
        # filtered_queryset = self.filter_queryset(queryset=self.get_queryset(topic))
        try:
            page = self.get_queryset(topic)
            text = page.content
            words = text.split()
            word_freq = {}
            for word in words:
                word = word.lower()  # Convert to lowercase to avoid duplicate word counts
                word_freq[word] = word_freq.get(word, 0) + 1
            # Sorting the words w.r.t frequency
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            # Slicing the top n words from the array of sorted word frequency wise
            top_n_words = sorted_words[:n]
            data = {
                "topic": topic,
                "top_words": {'Topic': topic, 'Top Words': top_n_words}
            }
            SearchHistory.objects.create(**data)
            return Response({'Topic': topic, 'Top Words': top_n_words}, status=status.HTTP_200_OK)
        except wikipedia.exceptions.PageError:
            return Response(ApplicationMessages.WIKI_PAGE_N_FOUND, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class GetSearchHistoryAPIView(generics.GenericAPIView):
    """Get wikipedia search history API View"""

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
        """Get all data from search history table"""
        return SearchHistory.objects.all()

    def get(self, request, *args, **kwargs):
        """Get Search History Data from Search history table"""
        try:
            filtered_queryset = self.filter_queryset(queryset=self.get_queryset())
            serializers = self.serializer_class(filtered_queryset, many=True)
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
