from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re

def get_info(soup):

    try:
        title = soup.find("span", attrs={"id":'productTitle'})
        title_value = title.text
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""
    
    try:
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

    except:
            price = ""
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""	


    return title_string, price, rating, review_count

def get_ASIN(soup):
    try:
        asin = soup.find("div", attrs={'class':'a-section table-padding'})
        print(asin)

    except AttributeError:
        asin = ""
    return asin

# def get_manufacturer():
    
#     try:
#         manu = soup.find("span", attrs={'class':'a-text-bold'}).string.strip()

#     except AttributeError:
#         manu = ""
#     return manu



if __name__ == '__main__':

    
    # HEADERS = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})
    # d = {"title":[], "price":[], "rating":[], "reviews":[], 'link':[]}
    
    # for i in range(1,21):
    #     URL = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{i}"

    #     webpage = requests.get(URL, headers=HEADERS)

    #     soup = BeautifulSoup(webpage.content, "html.parser")

    #     links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    #     links_list = []

    #     for link in links:
    #             links_list.append(link.get('href'))

    #     # d = {"title":[], "price":[], "rating":[], "reviews":[], 'link':[]}

    #     for link in links_list:
    #         new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

    #         new_soup = BeautifulSoup(new_webpage.content, "html.parser")
    #         title, price, rating, review_count = get_info(new_soup)

    #         d['title'].append(title) 
    #         d['price'].append(price) 
    #         d['rating'].append(rating)
    #         d['reviews'].append(review_count) #1
    #         d['link'].append("https://www.amazon.com" + link)
        
    # amazon_df = pd.DataFrame.from_dict(d)
    # amazon_df.to_csv("amazon_data.csv", header=True, index=False)
    
    df = pd.read_csv('amazon_data.csv')
    links = df['link']
    HEADERS = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})
    d = {"asin":[]}
    
    for link in range(0,200):
        URL = links[link]
        webpage = requests.get(URL, headers=HEADERS)

        soup = BeautifulSoup(webpage.content, "html.parser")
        # print(soup)
        asin_int = URL.find('B0')
        asin = URL[asin_int:asin_int+10]
        d['asin'].append(asin)
        # print(link)
        # break
            # d['price'].append(price) 
            # d['rating'].append(rating)
            # d['reviews'].append(review_count) #1
            # d['link'].append("https://www.amazon.com" + link)
        
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df.to_csv("product_asin.csv", header=True, index=False)
    