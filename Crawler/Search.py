from Page import Page
import json
# NOTE: time is only used in the __main__ portion of this script, the Search class does not use it
import time

class Search:


    def __init__(self, searchWord, refreshPages=False):

        # this is used to access other files within this directory
        # (we omit the end characters of __file__ to get rid of "Page.py" from the path)
        self.__currentDirectory = __file__[:-9]
        self.__websiteList = self.__getWebsiteList()
        # If refreshPages is True, then all tags for pages are refreshed
        if(refreshPages):
            self.__refreshPages()
        self.__searchWord = searchWord
        self.__pageData = self.__getPageData()
        self.__results = self.__searchResultsForTag()

    def __refreshPages(self):
        """ This refreshes all pages that are found in websites.json and updates their tags in pageData.json
            These pages are "refreshed" because when a new Page object is created, it automatically updates pageData.json """

        for page in self.__websiteList:
            # here, we create a Page object with the data we retrieved from websites.json
            Page(page["url"], page["pageName"])


    def __getWebsiteList(self):
        """ This returns a list of dictionaries that are website urls and names from websites.json """

        with open(f"{self.__currentDirectory}/jsonFiles/websites.json") as f:
            websiteList = json.load(f)
        return websiteList["websites"]


    def __getPageData(self):
        """ This returns a list of page data from pageData.json """

        with open(f"{self.__currentDirectory}/jsonFiles/pageData.json") as f:
            pageData = json.load(f)
        return pageData["pages"]

    def __searchResultsForTag(self):
        """ This searches for self.__searchWord in any tags within pageData.json
            It returns a list of tuples formatted (pageName, weight) """

        # this list will hold tuples of results
        results = []

        print(f"\nSearching {len(self.__pageData)} websites for \"{self.__searchWord}\" ...\n")

        for pd in self.__pageData:
            if(self.__searchWord in pd["weightedTags"]):
                print(f"Match found for \"{self.__searchWord}\" in \"{pd['pageName']}\"")
                results.append((pd["pageName"], pd["weightedTags"][self.__searchWord]))
        if(len(results) == 0):
            print(f"No matches found for \"{self.__searchWord}\"")

        # sort results in descending order for weight
        results.sort(key = lambda x: x[1], reverse=True)
        return results

    def getResults(self):
        return self.__results



if __name__ == "__main__":

    while True:
        print("\n\n\nSearch for any SINGLE word (no spaces) or \"r\" to refresh search data.")
        word = input("\nEnter word: ").lower()

        if(" " not in word):
            if(word == "r"):
                # timer
                startTime = time.perf_counter()
                print("\nRefreshing Search Data...")
                s = Search("", True)
                print("Search Data Refreshed!\n\n")
                stopTime = time.perf_counter()
                print(f"\nRefresh took {stopTime-startTime} seconds.\n")
                time.sleep(3)
            else:
                s = Search(word, False)
                print(s.getResults())
                break
