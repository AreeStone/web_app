from rest_framework import serializers

from news.models import Articles


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "anons",
            "full_text",
            "date",
        )
        model = Articles