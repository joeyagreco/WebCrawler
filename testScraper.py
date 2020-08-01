# Test Scraper

import requests
from bs4 import BeautifulSoup
from csv import writer
import lxml.html as lxml
import selenium
from selenium import webdriver
import time

def getTags(url):

	# THIS IS SO THE CHROME DRIVER DOES NOT POP UP
	# TO UNDO THIS, DELETE THE NEXT 3 LINES OF CODE AND REMOVE PARAMETERS FROM "driver = webdriver.Chrome(chrome_options=options)"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')


    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    print("\nConnection Opened.")
    print(f"Scraping: {url}\n")

    soup = BeautifulSoup(driver.page_source, 'lxml')

    # this one seems pretty useless ("span", "path", "meta", etc)
    #print([tag.name for tag in soup.find_all()])
    # this one just returns a lot of HTML jibberish
    #print([value for element in soup.find_all(class_=True) for value in element["class"]])

    # get all p tags and put them into a list
    pTags = soup.find_all("p")
    # list that will hold all tags
    tags = []
    for tagString in pTags:
        tagString = tagString.text
        for word in tagString.split():
            tags.append(word)

    # clean the tags
    tags = cleanTags(tags)
    print(tags)
    print("\nConnection Closed")


def cleanTags(tagList):
    """ This takes a list of strings (tags) and returns a 'clean' version of the list """

    badWords = ["and", "the", "to", "at", "for", "is", "a", "an", "by", "or", "in", "of", "but", "are", "on", "from"]
    # list that will hold all "cleaned" tags
    newTagList = []
    for tag in tagList:
        # make lowercase
        tag = tag.lower()
        # eliminate non alphabet characters
        for character in tag:
            if(not character.isalpha()):
                tag = tag.replace(character,"")
        # make sure a tag is only included if it isnt an empty string
        # and also that it isnt a "bad word"
        if(len(tag) > 0 and not tag in badWords):
            newTagList.append(tag)

    return newTagList










getTags("https://www.rd.com/jokes/")
