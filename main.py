import nltk

nltk.download('punkt')
import requests
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
import requests
#html source
url = 'https://www.motor-talk.de/suche.html?search&yfm=2019&se=Reichweite+Elektroauto'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')

#find h2 tag
find_all = soup.find_all('h2')

#print(find_all)


data = soup.find_all('h2')
#link = data[1]
nI = len(data)
print(nI)
urlarr = []

for i in range(1, nI-1):
  link_string = data[i].find_all('a')
  url = link_string[0].get('href')
  urlarr.append(url) 


url = 'https://www.motor-talk.de/forum/eine-woche-e-golf-ein-erfahrungsbericht-t5137826.html'

for url in urlarr:
  print(url)
  res = requests.get(url)
  html_page = res.content
  soup = BeautifulSoup(html_page, 'html.parser')
  text = soup.find_all(text=True)

  output = ''
  blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style'
    # there may be more elements you don't want, such as "style", etc.
  ] 

  for t in text:
      if t.parent.name not in blacklist:
         output += '{} '.format(t)

  text_output = nltk.tokenize.sent_tokenize(output)
#print('text_output: {0}'.format(text_output))
#print(len(text_output))
  sentences = nltk.sent_tokenize(output)
  result = [sentence for sentence in sentences if "Reichweite" in sentence]
  print(result)

import numpy as np 
np.savetxt("GFG.csv",  
           text_output, 
           delimiter =", ",  
           fmt ='% s') 