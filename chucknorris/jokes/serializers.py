from rest_framework import serializers

class JokeSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    joke_text = serializers.CharField()
    total = serializers.IntegerField()