import nltk

nltk.download('punkt')
import requests
from bs4 import BeautifulSoup

url = 'https://de.quora.com/Wenn-Du-Dich-f%C3%BCr-ein-Elektroauto-entscheiden-m%C3%BCsstest-welches-w%C3%A4re-es-und-warum'
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

print(output)


import nltk

nltk.download('punkt')
text = "This is a test. Let's try this sentence boundary detector."
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