from bs4 import BeautifulSoup
from selenium import webdriver
import json



class Crawler:

    def __init__(self, url):

        self.__url = url
        self.__soup = self.__getSoup()
        # this is used to access other files within this directory
        # (we omit the end characters of __file__ to get rid of "Crawler.py" from the path)
        self.__currentDirectory = __file__[:-10]
        self.__badTags = self.__getBadTags()


    def __getBadTags(self):
        """ This returns a list of bad tags from the "badTags.json" file """
        with open(f"{self.__currentDirectory}/jsonFiles/badTags.json") as f:
            badTagDict = json.load(f)
        return badTagDict["badTags"]


    def __getSoup(self):
        """ This returns the "soup" for self.__url """

        # THIS IS SO THE CHROME DRIVER DOES NOT POP UP
        # TO UNDO THIS, DELETE THE NEXT 3 LINES OF CODE AND REMOVE PARAMETERS FROM "driver = webdriver.Chrome(chrome_options=options)"
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')

        driver = webdriver.Chrome(chrome_options=options)
        driver.get(self.__url)

        print("\nConnection Opened.")
        print(f"\nScraping: {self.__url} ...\n")

        return BeautifulSoup(driver.page_source, 'lxml')

        print("\nConnection Closed.")


    def __getRawTags(self, tagType):
        """ This returns a list of raw tags as strings for the given tag type
            Tag type examples: "p", "h1", "h2"... """

        initialTags = self.__soup.find_all(tagType)

        return [it.text for it in initialTags]

    def __splitTags(self, tagList):
        """ This splits the tag strings in the given tag list
            Ex. ["hello world", "this is a test"] -> ["hello", "world", "this", "is", "a", "test"] """

        newTagList = []
        for tagString in tagList:
            for word in tagString.split():
                newTagList.append(word)
        return newTagList


    def __cleanTags(self, tagList):
        """ This "cleans" the given tag list
            It takes a list of string tags and returns a cleaned list """

        newTagList = []
        for tag in tagList:
            # make lowercase
            tag = tag.lower()
            # eliminate non alphabet characters
            for character in tag:
                if(not character.isalpha()):
                    # if a non-alphaber character is here, we replace that character with an empty string
                    tag = tag.replace(character,"")
            # make sure a tag is only included if it isnt an empty string
            # and also that it isnt a "bad word"
            if(len(tag) > 0 and not tag in self.__badTags):
                newTagList.append(tag)

        return newTagList

    def getTagList(self, tagType):
        """ This returns a fully-formatted tag list for the given tag type
            Tag type examples: "p", "h1", "h2"..."""

        rawTags = self.__getRawTags(tagType)
        splitTags = self.__splitTags(rawTags)
        cleanTags = self.__cleanTags(splitTags)
        return cleanTags
