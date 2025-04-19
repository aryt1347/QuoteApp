from rest_framework import serializers
from .models import QuotesModel

class QuotesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuotesModel
        fields = ['content', 'author', 'topic']