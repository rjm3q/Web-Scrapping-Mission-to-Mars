#import the stuff
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver

#chrome driver path
def init_browser():
    executable_path = {"executable_path":"C:\chromedriver_win32\chromedriver"}
    return Browser("chrome", **executable_path, headless = False)
#get to scraping
def scrape():
    browser= init_browser()
    marsdata={}
    NASA= "https://mars.nasa.gov/news/"
    browser.visit(NASA)
    time.sleep(3)
    html=browser.html
    soup=bs(html, 'mthl.parser')
    
    
#scrape da latest
    newsT = soup.find("div",class_="content_title").text
    newsP = soup.find("div", class_="article_teaser_body").text
    marsdata['Title'] = newsT
    marsdata['Paragragh'] = newsP
    
#mars pix
    image= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.vist(image)
    time.sleep=(3)
    html = browser.html
    soup = bs(html, 'lxml')

    full_image_button = soup.find(class_="button fancybox")
    browser.click_link_by_id('full_image')
    time.sleep(2)

    browser.click_link_by_partial_text('more info')
    browser.click_link_by_partial_text('.jpg')

    img_url = browser.url
    marsdata['Mars Image']= img_url
    
#red weather
    weather= 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather)
    html_weather = browser.html
    soup = bs(html_weather, "html.parser")
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    marsdata["mars_weather"] = mars_weather

#actual factual stuff
    facts= 'https://space-facts.com/mars/'
    browser.visit(facts_url)

    mfacts = pd.read_html(facts)
    mfacts = mfacts[1]
    mfacts = mfacts.rename(columns={0: 'Mars Planet Profile', 1: ''})
    mfacts.set_index('Mars Planet Profile')

    mars_html = mfacts.to_html(index=False, table_id='fact_table')
    marsdata['mars facts']= mars_html

#semi circles
    hemi= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.vist(hemi)
   
# dogdogdog
    links = soup.find_all('h3')
    browser.click_link_by_partial_text('Cerberus')
    time.sleep(1)
    browser.click_link_by_partial_text('Sample')
    browser.windows.current = browser.windows[1]
    cerberus_url = browser.url
    cerberus_dict = {
        'title': 'Cerberus Hemisphere',
        'img_url': cerberus_url
    }
    browser.windows[1].close()
    browser.back()
# Martin SKirelli
    browser.click_link_by_partial_text('Schiaparelli')
    time.sleep(1)
    browser.click_link_by_partial_text('Sample')
    browser.windows.current = browser.windows[1]
    schiaparelli_url = browser.url
    schiaparelli_dict = {
        'title': 'Schiaparelli Hemisphere',
        'img_url': schiaparelli_url
    }

    browser.windows[1].close()
    browser.back()
# A tune in SMajor
    browser.click_link_by_partial_text('Syrtis')
    time.sleep(1)
    browser.click_link_by_partial_text('Sample')
    browser.windows.current = browser.windows[1]
    syrtis_url = browser.url
    syrtis_dict = {
        'title': 'Syrtis Major Hemisphere',
        'img_url': syrtis_url
    }

    browser.windows[1].close()
    browser.back()
# Clever name No 4
    browser.click_link_by_partial_text('Valles')
    time.sleep(1)
    browser.click_link_by_partial_text('Sample')
    browser.windows.current = browser.windows[1]
    valles_url = browser.url
    valles_dict = {
        'title': 'Valles Marineris Hemisphere',
        'img_url': valles_url
    }
    browser.quit()
    
    hemisphere_earls= [cerberus_dict, schiaparelli_dict, syrtis_dict, valles_dict]
    marsdata['hemisphere_urls']= hemisphere_earls
#put it all together
    return marsdata
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    