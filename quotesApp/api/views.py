from django.shortcuts import render
from rest_framework import viewsets
from .models import QuotesModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from .serializers import QuotesModelSerializer

@api_view(['GET'])
def get_quote(request):
    quotes = QuotesModel.objects.all()
    
    # Returns on random quote at a time
    if quotes.exists():  
        quote = random.choice(quotes)
        serializer = QuotesModelSerializer(quote)
        return Response(serializer.data)
    
    return Response({"content": "N/A", "author": "N/A", "topic": "N/A"})


# For viewing all of the data
class QuotesViewSet(viewsets.ModelViewSet):
    queryset = QuotesModel.objects.all()
    serializer_class = QuotesModelSerializer
