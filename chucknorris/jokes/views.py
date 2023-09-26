from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .integrations import get_fetch_jokes
from .serializers import JokeSerializer

class JokeList(APIView):

    def get(self, request):
        joke_ids = set()
        jokes = []

        for _ in range(25):
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

        serializer = JokeSerializer(jokes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)