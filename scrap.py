import requests as rq
import pandas as pd
from bs4 import BeautifulSoup
import time
import sys


# get data using request

def get_html(url):
    html = rq.get(url)
    return html.content

def get_elemen(html,elemen):
    return BeautifulSoup(html,'html.parser').findAll(elemen)

# url = "https://www.tipsbelajarbahasainggris.com/kata-kerja-dalam-bahasa-inggris/"

url = sys.argv[1]
nameFile = sys.argv[2]
# print(get_html(url))
html = get_html(url)
numbers = []
verbs1 = []
verbs2 = []
verbs3 = []
vings = []

# get elemen

data = get_elemen(html,"tbody")
for el in data :
    
    for n in el.find_all("tr"):
        # search data
        no = n.find("td",attrs={'width':'63'})
        verb1 = n.find("td",attrs={'width':'119'})
        verb2 = n.find("td",attrs={'width':'104'})
        verb3 = n.find("td",attrs={'width':'107'})
        ving = n.find("td",attrs={'width':'112'})


        # set data
        # numbers.append(no.get_text())
        numbers.append(no.text)
        verbs1.append(verb1.text)
        verbs2.append(verb2.text)
        verbs3.append(verb3.text)
        vings.append(ving.text)

print("Parse Data....")

time.sleep(2)

print('Load Data...............')
time.sleep(1)    


# save to excel file
frame = {
    'Nomor' : numbers,
    'Verb1' : verbs1,
    'Verb2' : verbs2,
    'Verb3' : verbs3,
    'Ving' : vings
}
df = pd.DataFrame(frame)
df.to_excel(nameFile,index=False)

print("done..")

    

    
    
