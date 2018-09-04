from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import History

import re
import json
import datetime

from selenium import webdriver
from bs4 import BeautifulSoup



def index(request):
    return render(request, 'pttCrawler/index.html',)


def results(request):
    history_list = get_list_or_404(History)
    print(history_list)
    return render(request, 'pttCrawler/results.html', {'history_list': history_list})


def parse(request):
    driver = webdriver.PhantomJS()
    driver.get('https://www.ptt.cc/bbs/HardwareSale/index.html')
    soup = BeautifulSoup(driver.page_source, "html.parser")
    re_hs_title = re.compile(r'\[賣.*\].*(˙鍵帽|鍵盤|560|570|580|750|960|970|980|1060|1070|1080).*', re.I)
    re_hs_id = re.compile(r'.*\/HardwareSale\/M\.(\S+)\.html')

    match = []

    for article in soup.select('.r-list-container .r-ent .title a'):
        title = article.string
        if re_hs_title.match(title) != None:
            link = 'https://www.ptt.cc' + article.get('href')
            article_id = re_hs_id.match(link).group(1)
            match.append({'title': title, 'link': link, 'id': article_id})

    if len(match) > 0:
        history_list = History.objects.all()

        history_id_list = []
        for history in history_list:
            history_id_list.append(history.article_id)

        for article in match:
            if article['id'] in history_id_list:
                continue
            new_article = History(
                article_id=article['id'], article_title=article['title'], 
                article_link=article['link'], pub_date=timezone.now()
                )
            new_article.save()
            print(new_article)

    return HttpResponseRedirect(reverse('pttCrawler:results',))




