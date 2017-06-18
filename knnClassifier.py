#from math import log
import featureVector
from heapq import nlargest
import crawler
import urllib2
from bs4 import BeautifulSoup
from collections import defaultdict

articleSummaries=featureVector.getTrainingData()
print 'length of articleSummaries'
print len(articleSummaries)
testArticleSummary=featureVector.getTestingData()
print 'length of testArticleSummary'
print len(testArticleSummary)
print testArticleSummary
similarities={}
for articleUrl in articleSummaries:
    oneArticleSummary=articleSummaries[articleUrl]['feature-vector']
    similarities[articleUrl]=len(set(testArticleSummary).intersection(set(oneArticleSummary)))

labels= defaultdict(int)
knn=nlargest(5,similarities,key=similarities.get)
for oneNeighbour in knn:
    labels[articleSummaries[oneNeighbour]['label']]+=1

print nlargest(1,labels,key=labels.get)










#print len(articleSummaries)
#body =crawler.getWashPostText("https://www.washingtonpost.com/politics/help-wanted-why-republicans-wont-work-for-the-trump-administration/2017/06/17/61e3d33e-506a-11e7-b064-828ba60fbb98_story.html?utm_term=.85d3b1224783",'article')
#print body[0]
#body=crawler.getNYText("https://www.nytimes.com/2017/06/18/us/politics/michael-flynn-intel-group-trump.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news&_r=0",None)
#print body[0]
#page=urllib2.urlopen("https://www.nytimes.com/2017/06/17/style/father-daughter-dance-same-sex-couples-single-parents.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=photo-spot-region&region=top-news&WT.nav=top-news").read().decode('utf8')
#print page
#page =urllib2.urlopen("https://www.washingtonpost.com/sports/?nid=top_nav_sports&utm_term=.cd5801bd0098").read().decode("utf8")
#print page
#url="https://www.washingtonpost.com/sports/?nid=top_nav_sports&utm_term=.cd5801bd0098"
#headers={'authority':'www.washingtonpost.com'
#,'method':'GET'
#,'path':'/sports/?nid=top_nav_sports&utm_term=.cd5801bd0098'
#,'scheme':'https'
#,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
#,'accept-encoding':'gzip, deflate, sdch, br'
#,'accept-language':'en-US,en;q=0.8'
#,'cache-control':'max-age=0'
#,'cookie':'de=; rplpwabt3=0; rpld0=1:06|; __gads=ID=3c56ff20401cfaa7:T=1497612377:S=ALNI_Mav7RN7vooI5HoDQj44nhFl8ccl0g; washpost_poe=true; region_cookie=0; devicetype=0; rplmct=2; client_region=0; rpld1=20:ind|21:mh|22:mumbai|23:18.942060|24:72.835442|0:jio.com|; _chartbeat2=.1497612374971.1497784804512.101.ECJUVBV92hqDrh0I6CaMeMBzXpab; #s_pers=%20s_vmonthnum%3D1498847400755%2526vn%253D4%7C1498847400755%3B%20s_nr%3D1497784806655-Repeat%7C1500376806655%3B%20s_lv%3D1497784806659%7C1592392806659%3B%20s_lv_s%3DLess%2520than%25201%2520day%7C1497786606659%3B%20s_monthinvisit%3Dtrue%7C1497786606685%3B%20gvp_p5%3Dfront%2520-%2520%252Fsports%7C1497786606709%3B%20gvp_p51%3Dwp%2520-%2520sports%7C1497786606735%3B; s_vi=[CS]v1|2CA1E02D85032BAC-4000118200003B7F[CE]; devicetype=0; osfam=0; #s_sess=%20s_wp_ep%3Dhomepage%3B%20s._ref%3DDirect-Load%3B%20s_cc%3Dtrue%3B%20s_dslv%3DLess%2520than%25201%2520day%3B%20s_sq%3D%3B%20s_ppvl%3Dpolitics%25253Aarticle%252520-%252520828ba60fbb98%252520-%25252020170618%252520-%252520help-wanted-why-republicans-wont-work-for-the-trump-administration%252C8%252C8%252C678%252C1301%252C678%252C1366%252C768%252C1%252CP%3B%20s_ppv%3Dfront%252520-%252520%252Fsports%252C5%252C5%252C463%252C1301%252C463%252C1366%252C768%252C1%252CP%3B'
#,'referer':'https://www.washingtonpost.com/'
#,'upgrade-insecure-requests':'1'
#,'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
#header={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
#response=urllib2.Request(url,headers=header)
#try:
#    page=urllib2.urlopen(response)
#    soup=BeautifulSoup(page)
#    for a in soup.find_all('a'):
#        url=a.get('href')
#        url=str(url)
#        if 'https' in url and '2017' in url:
#            body=crawler.getWashPostText(url,"article")
#            print body[1]
#except urllib2.HTTPError, e:
#    print 'error'
