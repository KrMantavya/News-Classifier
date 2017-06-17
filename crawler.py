import requests
import urllib2
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from math import log
from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.cluster import Kmeans

def getWashPostText(url,token):
    try:
        page=urllib2.urlopen(url).read().decode('utf8')
    except:
        return (None,None)
    soup=BeautifulSoup(page)
    if soup is None:
        return (None,None)
    text =""
    if soup.find_all(token) is not None:
        text=' '.join(map(lambda p:p.text, soup.find_all(token)))
        soup2=BeautifulSoup(text)
        if soup2.find_all('p') is not None:
            text=' '.join(map(lambdaa p: p.text, soup2.find_all('p')))
        return text, soup.title.text

def getNYText(url,token):
    response=resquest.get(url)
    soup=BeautifulSoup(response.content)
    page=str(soup)
    title=soup.find('title').text
    mydivs=soup.findAll("p":{"class":"story-body-text"})
    text=' '.join(map(lambda p:p.text,mydivs))
    return text,title

def scrapeSource(url, magicFrag='2017',scrapperFunction=getNYText,token='None'):
    urlBodies={}
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)
    soup=BeautifulSoup(response)
    for a in soup.findAll('a'):
        try:
            url=a['href']
            if((url not in urlBodies) and (magicFrag is not None and magicFrag in url) or magicFrag is None):
                body =scraperFunction(url,token)
                if body and len(body)>0:
                    urlBodies[url]=body
                    print url
                except:
                    numErrors+=1
