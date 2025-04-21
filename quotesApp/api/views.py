from django.shortcuts import render
from rest_framework import viewsets
from .models import QuotesModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from .serializers import QuotesModelSerializer
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# View to do some web scraping
# Wikipedia page the author and insert bio or go to wikipedia link
def scrape_author_wiki(authorName):

    url = "https://en.wikipedia.org/wiki/" + authorName.replace(" ", "_")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all("p")
    
    for p in paragraphs:
        if p.find("b"):
            soup = p
            # Remove all <sup> tags
            for sup in soup.find_all('sup'):
                sup.decompose()

            # Get cleaned text
            cleaned_bio = soup.get_text(strip=True)
            return cleaned_bio

def index(request):
    return render(request, "index.html")

@api_view(['GET'])
def get_quote(request):
    quotes = QuotesModel.objects.all()
    
    # Returns on random quote at a time
    if quotes.exists():  
        quote = random.choice(quotes)
        bio  = scrape_author_wiki(quote.author)
        serializer = QuotesModelSerializer(quote)
        data_with_bio = serializer.data
        data_with_bio["bio"] = bio
        return Response(data_with_bio)
    
    return Response({"content": "N/A", "author": "N/A", "topic": "N/A"})


# For viewing all of the data
class QuotesViewSet(viewsets.ModelViewSet):
    queryset = QuotesModel.objects.all()
    serializer_class = QuotesModelSerializer
