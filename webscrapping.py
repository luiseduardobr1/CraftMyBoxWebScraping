import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
#import matplotlib.pyplot as plt

# Initialize browser
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# Get website
thing_url = "https://craftmybox.com/placas-video"
driver.get(thing_url)

# Search
searchbox = driver.find_element_by_css_selector("input[placeholder='Procurar placas de vídeo...']");
searchbox.click()
searchbox.send_keys("rtx 2080")

# Get source code (HTML)
time.sleep(5)
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, "html.parser")
soup.find('table', attrs={'class': 'table is-responsive is-touch js-data-table'})

# Initialize lists
nome=[]
memoria=[]
preco=[]

# Name of the product
for line in soup.findAll('div', attrs={'class': 'is-flex-widescreen is-vcentered'}):
    nomet=line.text
    nomet=" ".join(nomet.split()) #Delete duplicates whitespace and newline characters
    nome.append(nomet)
#print(nome)
    
# Memory of the product
for line in soup.findAll('td', attrs={'data-label': 'Memória'}):
    memoriat=line.text
    memoriat=" ".join(memoriat.split())
    memoria.append(memoriat)
#print(memoria)


# Price of the product
for line in soup.findAll('td', attrs={'data-label': 'Preço boleto'}):
    preco2=line.text
    preco2=preco2.replace('R$','')
    preco2=preco2.replace('.','')
    preco2=preco2.replace(',','.')
    preco2=" ".join(preco2.split())
    preco.append(preco2)
#print(preco)

# Number of elements
nmem=len(memoria)

# Get Data/Time
data1=time.strftime("%d/%m/%Y %H:%M:%S")


for i in range(0,nmem):
    combinacao=[data1,nome[i],memoria[i],preco[i]]
    df=pd.DataFrame(combinacao)
    with open('craftmybox-TESTEFINAL.csv', 'a') as f:
        df.transpose().to_csv(f, header=False)

driver.quit()  

# Reading data in *.csv file 
colnames=['Zeros', 'Data', 'Produto', 'Memória', 'Preço'] 
data = pd.read_csv("craftmybox-TESTEFINAL.csv", encoding='ISO-8859-1', names=colnames, header=None) 
data=data.T[data.any()].T #delete zero's column
data = data.sort_values(by=['Preço','Data'], ascending=[True, False])

data