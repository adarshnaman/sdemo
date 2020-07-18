import requests

from bs4 import BeautifulSoup
def hitapi(res):
    
    soup=BeautifulSoup(res.text,'html.parser')
    link=soup.select('.storylink')
    score=soup.select('.subtext')  
    
    return createcos(link, score)


def createcos(link,score):
    hn=[]
    for i,item in enumerate(link):
        title=link[i].getText()
        links=link[i].get('href',None)
        votes=score[i].select('.score')
        if len(votes):
            point=int(votes[0].getText().replace(" points",""))
            if point>99:
                hn.append({'title':title,'links':links,'point':point})
    hn.sort(key=lambda k:k['point'],reverse=True)
    return hn


page=int(input("enter the page number to grab data : "))
res=requests.get(f'https://news.ycombinator.com/news?p={page}')
hitapi(res)
for i in hitapi(res):
    print(i,"\n")

