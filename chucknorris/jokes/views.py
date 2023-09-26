import time
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from concurrent.futures import ThreadPoolExecutor
from .integrations import get_fetch_jokes
from .serializers import JokeSerializer

class JokeList(APIView):

    def get(self, request):
        joke_ids = set()
        jokes = []

        def fetch_and_append(_):
            joke_id, joke_value = get_fetch_jokes()
            if joke_id not in joke_ids:
                joke_ids.add(joke_id)
                jokes.append(
                    {
                        'id': joke_id,
                        'joke_text': joke_value,
                        'total': len(joke_ids)
                    }
                )
        with ThreadPoolExecutor(max_workers=25) as executor:
            executor.map(fetch_and_append, range(25))

        serializer = JokeSerializer(jokes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)