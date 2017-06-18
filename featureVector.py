from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import crawler

class FeatureExtractor:
    def __init__(self,min_cut=0.1,max_cut=0.9):
        self._min_cut=min_cut
        self._max_cut=max_cut
        self._stopwords=set(stopwords.words('english')+list(punctuation)+[u"'s",'"'])

    def _compute_frequencies(self,word_sent,customStopwords=None):
        freq=defaultdict(int)
        if customStopwords is None:
            stopwords=set(self._stopwords)
        else:
            stopwords=set(customStopwords).union(self._stopwords)
        for sentence in word_sent:
            for word in sentence:
                if word not in stopwords:
                    freq[word]+=1
        m=float(max(freq.values()))
        for word in freq.keys():
            freq[word]=freq[word]/m
            if freq[word]>=self._max_cut or freq[word]<= self._min_cut:
                del freq[word]
        return freq

    def _extractFeatures(self,article,n,customStopwords=None):
        text=article[0]
        title=article[1]
        sentences=sent_tokenize(text)
        word_sent=[word_tokenize(s.lower()) for s in sentences]
        self._freq=self._compute_frequencies(word_sent,customStopwords)
        if n<0:
            return nlargest(len(self._freq),self._freq,key=self._freq.get)
        else:
            return nlargest(n,self._freq,key=self._freq.get)

    def _extractRawFrequencies(self,article):
        text=article[0]
        title=article[1]
        sentences=sent_tokenize(text)
        word_sent=[word_tokenize(s.lower()) for s in sentences]
        freq=defaultdict(int)
        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word]+=1
        return freq

    def _summarize(self,article,n):
        text=article[0]
        title=aricle[1]
        sentences=sent-tokenize(text)
        word_sent=[word_tokenize(s.lower()) for s in sentences]
        self._freq=self._compute_frequencies(word_sent)
        rankinf=deafaultdict(int)
        for i,sentences in enumerate(word_sent):
            for word in sentences:
                if word in self._freq:
                    ranking[i]+=self.freq[word]
        sentences_index=nlargest(n,ranking,key=ranking.get)
        return [sentences[j] for j in sentences_index]

def getTrainingData():
    washingtonPostSports="https://www.washingtonpost.com/sports/?nid=top_nav_sports&utm_term=.b8d5cc9afa06"
    nytimesSports="https://www.nytimes.com/section/sports?WT.nav=page&action=click&contentCollection=Sports&module=HPMiniNav&pgtype=Homepage&region=TopBar"
    washingtonPostTech="https://www.washingtonpost.com/business/technology/?nid=top_nav_tech&utm_term=.e44b05f06b09"
    nytimesTech="https://www.nytimes.com/section/technology?WT.nav=page&action=click&contentCollection=Tech&module=HPMiniNav&pgtype=Homepage&region=TopBar"

    washingtonPostTechArticles=crawler.scrapeSource(washingtonPostTech,'2017','getWashPostText','article')
    washingtonPostNonTechArticles=crawler.scrapeSource(washingtonPostSports,'2017','getWashPostText','article')
    #nyTimesTechArticles=crawler.scrapeSource(nytimesTech,'2017','getNYText',None)
    #nyTimesNonTechArticles=crawler.scrapeSource(nytimesSports,'2017','getNYText',None)

    articleSummaries={}
    for techUrlDictionary in [washingtonPostTechArticles]:
        for articleUrl in techUrlDictionary:
            if len(techUrlDictionary[articleUrl][0])>1:
                fs=FeatureExtractor()
                summary=fs._extractFeatures(techUrlDictionary[articleUrl],25)
                articleSummaries[articleUrl]={'feature-vector':summary,'label':'Tech'}

    for nontechUrlDictionary in [washingtonPostNonTechArticles]:
        for articleUrl in nontechUrlDictionary:
            if len(nontechUrlDictionary[articleUrl][0])>1:
                fs=FeatureExtractor()
                summary=fs._extractFeatures(nontechUrlDictionary[articleUrl],25)
                articleSummaries[articleUrl]={'feature-vector':summary,'label':'NonTech'}
    return articleSummaries

def getTestingData():
    testUrl="https://www.washingtonpost.com/politics/help-wanted-why-republicans-wont-work-for-the-trump-administration/2017/06/17/61e3d33e-506a-11e7-b064-828ba60fbb98_story.html?utm_term=.848aee1f0126"
    testArticle=crawler.getWashPostText(testUrl,"article")
    print type(testArticle[0])
    fs=FeatureExtractor()
    testArticleSummary=fs._extractFeatures(testArticle, 25)
    #print testArticleSummary
    return testArticleSummary

def getTechArticles():
    washingtonPostSports="https://www.washingtonpost.com/sports/?nid=top_nav_sports&utm_term=.b8d5cc9afa06"
    nytimesSports="https://www.nytimes.com/section/sports?WT.nav=page&action=click&contentCollection=Sports&module=HPMiniNav&pgtype=Homepage&region=TopBar"
    washingtonPostTech="https://www.washingtonpost.com/business/technology/?nid=top_nav_tech&utm_term=.e44b05f06b09"
    nytimesTech="https://www.nytimes.com/section/technology?WT.nav=page&action=click&contentCollection=Tech&module=HPMiniNav&pgtype=Homepage&region=TopBar"

    washingtonPostTechArticles=crawler.scrapeSource(washingtonPostTech,'2017','getWashPostText','article')
    #washingtonPostNonTechArticles=crawler.scrapeSource(washingtonPostSports,'2017','getWashPostText','article')
    return washingtonPostTechArticles

def getNonTechArticles():
    washingtonPostSports="https://www.washingtonpost.com/sports/?nid=top_nav_sports&utm_term=.b8d5cc9afa06"
    nytimesSports="https://www.nytimes.com/section/sports?WT.nav=page&action=click&contentCollection=Sports&module=HPMiniNav&pgtype=Homepage&region=TopBar"
    washingtonPostTech="https://www.washingtonpost.com/business/technology/?nid=top_nav_tech&utm_term=.e44b05f06b09"
    nytimesTech="https://www.nytimes.com/section/technology?WT.nav=page&action=click&contentCollection=Tech&module=HPMiniNav&pgtype=Homepage&region=TopBar"

    #washingtonPostTechArticles=crawler.scrapeSource(washingtonPostTech,'2017','getWashPostText','article')
    washingtonPostNonTechArticles=crawler.scrapeSource(washingtonPostSports,'2017','getWashPostText','article')
    return washingtonPostNonTechArticles
