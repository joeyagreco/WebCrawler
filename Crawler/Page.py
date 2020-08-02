from Weigher import Weigher
import json

class Page:

    def __init__(self, url, pageName):

        self.__url = url
        self.__pageName = pageName
        self.__weigher = Weigher(self.__url)
        self.__weightedTags = self.__weigher.getWeightedTags()
        # this is used to access other files within this directory
        # (we omit the end characters of __file__ to get rid of "Page.py" from the path)
        self.__currentDirectory = __file__[:-7]
        self.__pageData = self.__getPageData()
        self.__savePageData()


    def __getPageData(self):
        """ This returns a list of all page data in pageData.json """

        with open(f"{self.__currentDirectory}/jsonFiles/pageData.json") as f:
            pageData = json.load(f)
        return pageData["pages"]

    def __savePageData(self):
        """ This updates the record in pageData.json for this page """

        print(f"\nUpdating page data in pageData.json for page: \"{self.__pageName}\" ...")
        # variable to keep track of if we have found this Page's data within pageData.json
        inData = False
        # first, check if data for this page already exists in pageData.json, and if so, replace it
        for i, pageRecord in enumerate(self.__pageData):
            if(self.__url == pageRecord["url"]):
                # we found a match, now replace it
                self.__pageData[i] = {"url": self.__url, "pageName": self.__pageName, "weightedTags": self.__weightedTags}
                inData = True
        if(not inData):
            # we reach this if there isnt a record of this Page in pageData.json
            # here, we append the data to the list of page data records
            self.__pageData.append({"url": self.__url, "pageName": self.__pageName, "weightedTags": self.__weightedTags})

        # now, we update the pageData.json file
        with open(f"{self.__currentDirectory}/jsonFiles/pageData.json", "w") as f:
            json.dump({"pages": self.__pageData}, f, indent=4)

    def getUrl(self):
        return self.__url

    def getPageName(self):
        return self.__pageName

    def getWeightedTags(self):
        return self.__weightedTags


if __name__ == "__main__":
    #p = Page("https://www.move2thejunction.com/", "The Junction")
    #p = Page("https://atom.io/", "Atom")
    pass
