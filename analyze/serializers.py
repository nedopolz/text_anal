from rest_framework import serializers
from main.utils import analyse_text


class TextInputSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=3000)

    def create(self, validated_data: dict):
        text = validated_data.get("text")
        return analyse_text(text)
