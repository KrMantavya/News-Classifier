import requests
import urllib2
from bs4 import BeautifulSoup
#from sklearn.feature_extraction.text import TfidVectorizer
#from sklearn.cluster import Kmeans

def getWashPostText(url,token):
    #try:
    #    page=urllib2.urlopen(url).read().decode('utf8')
    #except:
    #    return (None,None)
    header={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
    response=urllib2.Request(url,headers=header)
    try:
        page=urllib2.urlopen(response)
    except urllib2.HTTPError, e:
        print 'error'
        return (None,None)
    print 'page obtained'
    soup=BeautifulSoup(page)
    if soup is None:
        print 'error'
        return (None,None)
    text =""
    if soup.find_all(token) is not None:
        text=' '.join(map(lambda p:p.text, soup.find_all(token)))
        soup2=BeautifulSoup(text)
        if soup2.find_all('p') is not None:
            text=' '.join(map(lambda p: p.text, soup2.find_all('p')))
        return text, soup.title.text

def getNYText(url,token):
    try:
        page=urllib2.urlopen(url).read().decode('utf8')
    except:
        return ("error",None)
    #response=resquest.get(url)
    #soup=BeautifulSoup(response.content)
    #page=str(soup)
    soup=BeautifulSoup(page)
    if soup is None:
        return (None,None)
    title=soup.find('title').text
    mydivs=soup.find_all("p",{"class":"story-body-text"})
    text=' '.join(map(lambda p:p.text,mydivs))
    return text,title

def scrapeSource(url, magicFrag='2017',scrapperFunction='getNYText',token='None'):
    urlBodies={}
    #try:
    #    page=urllib2.urlopen(url).read().decode('utf8')
    #except:
    #    return urlBodies
    #request=urllib2.Request(url)
    #response=urllib2.urlopen(request)
    #soup=BeautifulSoup(response)
    header={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
    response=urllib2.Request(url,headers=header)
    try:
        page=urllib2.urlopen(response)
    except:
        print 'error'
        return urlBodies

    soup=BeautifulSoup(page)
    if soup is None:
        return (None)
    numErrors=0
    for a in soup.find_all('a'):
        url=a.get('href')
        url=str(url)
        if 'https' in url and '2017' in url:
            body=getWashPostText(url,"article")
            print body[1]
            if body[0]!=None:
                urlBodies[url]=body
    return urlBodies

def getDoxyDonkeyText(testUrl,token):
    #response=requests.get(testUrl)
    #soup=BeautifulSoup(response.content)
    #page=str(soup)
    try:
        page=urllib2.urlopen(url).read().decode('utf8')
    except:
        return (None,None)
    soup=BeautifulSoup(page)
    if soup is None:
        return (None,None)
    title=soup.fin("title").text
    mydivs=soup.find_all("div",{"class":token})
    text=' '.join(map(lambda p: p.text, mydivs))
    return text,title
