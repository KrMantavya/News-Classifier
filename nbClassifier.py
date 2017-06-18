#from math import log
import featureVector
from heapq import nlargest
import crawler
import urllib2
from bs4 import BeautifulSoup
from collections import defaultdict

cumulativeRawFrequencies={'Tech':defaultdict(int),'NonTech':defaultdict(int)}
techArticles=featureVector.getTechArticles()
nontechArticles=featureVector.getNonTechArticles()
trainingData={'Tech':techArticles,'NonTech':nontechArticles}
for label in trainingData:
    for articleUrl in trainingData[label]:
        if trainingData[label][articleUrl][0]!=None:
            fs=featureVector.FeatureExtractor()
            rawFrequencies=fs._extractRawFrequencies(trainingData[label][articleUrl])
            for word in rawFrequencies:
                cumulativeRawFrequencies[label][word]+=rawFrequencies[word]

techiness=1.0
nontechiness=1.0
testArticleSummary=featureVector.getTestingData()
for word in testArticleSummary:
    if word in cumulativeRawFrequencies['Tech']:
        techiness*=1e3*cumulativeRawFrequencies['Tech'][word]/float(sum(cumulativeRawFrequencies['Tech'].values()))
    else:
        techiness/=1e3

for word in testArticleSummary:
    if word in cumulativeRawFrequencies['NonTech']:
        nontechiness*=1e3*cumulativeRawFrequencies['NonTech'][word]/float(sum(cumulativeRawFrequencies['NonTech'].values()))
    else:
        nontechiness/=1e3

techiness*=float(sum(cumulativeRawFrequencies['Tech'].values()))/(float(sum(cumulativeRawFrequencies['Tech'].values()))+float(sum(cumulativeRawFrequencies['NonTech'].values())))
nontechiness*=float(sum(cumulativeRawFrequencies['NonTech'].values()))/(float(sum(cumulativeRawFrequencies['Tech'].values()))+float(sum(cumulativeRawFrequencies['NonTech'].values())))

if techiness>=nontechiness:
    print 'Tech'
else:
    print 'NonTech'
