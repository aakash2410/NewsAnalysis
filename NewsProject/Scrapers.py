from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
import time
def TOI(search_term):
    df=[]
    for i in range(1, 3):
        source = get(f'https://timesofindia.indiatimes.com/topic/{search_term}/{str(i)}')
        soup = BeautifulSoup(source.text, "html.parser")
        for headlines in soup.find_all('span',class_='title'):
            headline=headlines.text
            df.append(headline)
        for headlines in soup.find_all('div',class_='overlay'):
            headline=headlines.span.text
            df.append(headline)
    new_df=[]
    for i in df:
        i=i[1:-1]
        new_df.append(str(i))
    new_df = pd.DataFrame(new_df, columns = ["Headlines"])
    return new_df

def NDTV(search_term):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(f'https://www.ndtv.com/search?searchtext={search_term}')
    load_more=driver.find_element_by_class_name('loadmore_btn')
    df=[]
    w=0
    source=get(f'https://www.ndtv.com/search?searchtext={search_term}')
    soup=BeautifulSoup(source.text,'html.parser')
    number = soup.find('div',class_="search_title_box").span.text
    numbers = []
    for word in number.split():
        if word.isdigit():
            numbers.append(int(word))
    for i in numbers:
        k=int(i)
    k=k//15
    for x in range(k):
        if load_more.is_displayed():
            driver.execute_script("arguments[0].click();", load_more)
            time.sleep(1)
    source=driver.page_source
    soup=BeautifulSoup(source,'html.parser')
    for headlines in soup.find_all('p',class_='header fbld'):
        headline=headlines.a.strong.text
        df.append(headline)
        w+=1
    return df

def IndiaTV(search_term):
    df=[]
    w=0
    for i in range(1,20):
        source=get(f'https://www.indiatvnews.com/topic/{search_term}/{i}')
        soup = BeautifulSoup(source.text, "html.parser")
        for headlines in soup.find_all('h3',class_='title'):
            headline=headlines.a.text
            df.append(headline)
            w+=1
    return df

def IndianExpress(search_term):
    df=[]
    w=0
    for i in range(1,20):
        source = get(f'https://indianexpress.com/page/{i}/?s={search_term}')
        soup = BeautifulSoup(source.text,'html.parser')
        for headlines in soup.find_all('div',class_='details'):
            headline = str(headlines.h3)
            headline=headline.split('">')
            headline=headline[:-9] 
            df.append(headline)
            w+=1
    return df

def TheHindu(search_term):
    df=[]
    w=0
    for i in range(1,30):
        source = get(f'https://www.thehindu.com/search/?q={search_term}&order=DESC&sort=publishdate&page={i}')
        soup = BeautifulSoup(source.text,'html.parser')
        for headlines in soup.find_all('a',class_='story-card75x1-text'):
            headline=headlines.text
            df.append(headline)
            w+=1
    return df
    


    



