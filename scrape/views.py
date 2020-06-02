from django.shortcuts import render
from django.http import HttpResponse
from .tasks import scrape
import requests
from bs4 import BeautifulSoup
from . import models


def index(request):
    li_to_fetch = ['https://www.indiatoday.in/rss/1206514', 'https://www.indiatoday.in/rss/1206614', 'https://www.indiatoday.in/rss/1206584', 'https://www.indiatoday.in/rss/1206513', 'https://www.indiatoday.in/rss/1206577', 'https://feeds.feedburner.com/ndtvnews-top-stories', 'https://feeds.feedburner.com/ndtvnews-latest', 'https://feeds.feedburner.com/ndtvnews-india-news', 'https://feeds.feedburner.com/ndtvnews-world-news', 'https://feeds.feedburner.com/ndtvprofit-latest']
    for i in li_to_fetch:
        print (i)
        scrape.delay(i)
    data = models.News.objects.all()
    context = {
        'data':data,
    }
    return render(request, 'index.html', context)