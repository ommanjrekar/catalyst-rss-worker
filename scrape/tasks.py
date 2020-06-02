from celery import Celery, shared_task
from time import sleep
import requests
from bs4 import BeautifulSoup
import re
from .models import News

app = Celery()

@shared_task
def scrape(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    for x in soup.find_all('item'):
        t = x.title.string
        if News.objects.filter(title=t).exists():
            break
        else:
            title = x.title.string
            date = x.pubdate.string
            desc = x.description.string
            x = str(x)
            link = re.findall(r'<link/><!\[.*\[\s*(.*?)\s*\]', x)
            link = ''.join(link)
            News.objects.create(title=title, description=desc, date=date, url=link)


    return res.status_code
